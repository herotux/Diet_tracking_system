from rest_framework import serializers
from apps.users.models import User
from apps.programs.models import Program, Task, Progress

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'role',
            'national_id', 'birth_date', 'gender', 'phone_number', 'address',
            'height_cm', 'weight_kg', 'activity_level', 'goal',
            'specialty', 'license_number', 'clinic_address'
        )

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'email', 'first_name', 'last_name', 'role',
            'national_id', 'birth_date', 'gender', 'phone_number', 'address'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data['role'],
            national_id=validated_data.get('national_id'),
            birth_date=validated_data.get('birth_date'),
            gender=validated_data.get('gender'),
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address')
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