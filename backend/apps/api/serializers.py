from rest_framework import serializers
from apps.users.models import User
from apps.programs.models import Program, Task, Progress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'role')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role']
        )
        return user

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'day_of_week')

class ProgramSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    doctor = UserSerializer(read_only=True)
    patients = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Program
        fields = ('id', 'name', 'description', 'program_type', 'doctor', 'patients', 'tasks')

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ('id', 'task', 'patient', 'status', 'note', 'date', 'updated_at')
        read_only_fields = ('patient',)