from django.core.management.base import BaseCommand
from main_app.models import CustomUser, Admin, Staff, Student

class Command(BaseCommand):
    help = 'Create default users'

    def handle(self, *args, **kwargs):
        # Create Admin
        admin_email = "admin@gmail.com"
        if not CustomUser.objects.filter(email=admin_email).exists():
            admin = CustomUser.objects.create(
                email=admin_email,
                user_type='1',  # HOD
                first_name='Admin',
                last_name='User',
                gender='M',
                address='Admin Address'
            )
            Admin.objects.create(admin=admin)
            self.stdout.write(f'Created admin user with email: {admin_email}')

        # Create Staff
        staff_email = "staff@gmail.com"
        if not CustomUser.objects.filter(email=staff_email).exists():
            staff_user = CustomUser.objects.create(
                email=staff_email,
                user_type='2',  # Staff
                first_name='Staff',
                last_name='User',
                gender='M',
                address='Staff Address'
            )
            Staff.objects.create(admin=staff_user)
            self.stdout.write(f'Created staff user with email: {staff_email}')

        # Create Student
        student_email = "student@gmail.com"
        if not CustomUser.objects.filter(email=student_email).exists():
            student_user = CustomUser.objects.create(
                email=student_email,
                user_type='3',  # Student
                first_name='Student',
                last_name='User',
                gender='M',
                address='Student Address'
            )
            Student.objects.create(admin=student_user)
            self.stdout.write(f'Created student user with email: {student_email}')
