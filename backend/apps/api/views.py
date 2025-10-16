from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from django.db.models import Count
from apps.users.models import User
from apps.programs.models import Program, Progress, Task
from .serializers import (
    RegisterSerializer, UserSerializer, ProgramSerializer, ProgressSerializer
)
from .permissions import IsDoctor, IsPatient

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'DOCTOR':
            return Program.objects.filter(doctor=user)
        elif user.role == 'PATIENT':
            return user.assigned_programs.all()
        return Program.objects.none()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsDoctor]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)

class ProgressViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    permission_classes = [IsPatient]

    def get_queryset(self):
        return Progress.objects.filter(patient=self.request.user)

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class ProgressSummaryView(generics.GenericAPIView):
    permission_classes = [IsDoctor]

    def get(self, request, *args, **kwargs):
        program_id = self.kwargs.get('program_id')
        try:
            program = Program.objects.get(id=program_id, doctor=request.user)
        except Program.DoesNotExist:
            return Response({"detail": "Not found."}, status=404)

        summary = {}
        for patient in program.patients.all():
            total_tasks = Task.objects.filter(program=program).count()
            completed_tasks = Progress.objects.filter(
                task__program=program,
                patient=patient,
                status__in=['COMPLETED', 'PARTIALLY_COMPLETED']
            ).count()
            adherence = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

            summary[patient.username] = {
                'total_tasks': total_tasks,
                'completed_tasks': completed_tasks,
                'adherence': adherence,
            }
        return Response(summary)

class LanguageListView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        from django.conf import settings
        return Response(settings.LANGUAGES)