from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Program, Task

User = get_user_model()

class ProgramTestCase(TestCase):
    def setUp(self):
        self.doctor = User.objects.create_user(username='doctor', password='password', role='DOCTOR')
        self.patient = User.objects.create_user(username='patient', password='password', role='PATIENT')
        self.program = Program.objects.create(name='Test Program', program_type='DIET', doctor=self.doctor)
        self.program.patients.add(self.patient)
        self.task = Task.objects.create(program=self.program, name='Test Task', day_of_week=1)

    def test_program_creation(self):
        self.assertEqual(self.program.name, 'Test Program')
        self.assertEqual(self.program.doctor, self.doctor)
        self.assertEqual(self.program.patients.first(), self.patient)

    def test_task_creation(self):
        self.assertEqual(self.task.name, 'Test Task')
        self.assertEqual(self.task.program, self.program)