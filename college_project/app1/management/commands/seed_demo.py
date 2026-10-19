"""Fill the database with demo data so visitors can try the app right away.

Usage: python manage.py seed_demo
Safe to run more than once: existing demo records are reused.
"""
from datetime import date, timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from app1.models import Course, Student, Teacher

COURSES = [('BCA', 45000), ('B.Com', 38000), ('BBA', 42000), ('B.Sc Computer Science', 48000), ('MCA', 65000)]

TEACHERS = [
    # username, first, last, course, age, phone, photo
    ('anjali', 'Anjali', 'Menon', 'BCA', 34, '9400000001', 'images/person2.jpg'),
    ('rohan', 'Rohan', 'Thomas', 'B.Com', 41, '9400000002', 'images/person3.jpg'),
    ('meera', 'Meera', 'Nair', 'MCA', 38, '9400000003', 'images/person4.jpg'),
]

STUDENTS = [
    ('Arjun K', 'Kozhikode', 19, 'BCA', 60), ('Fathima R', 'Malappuram', 20, 'BCA', 300),
    ('Nikhil P', 'Thrissur', 21, 'B.Com', 120), ('Sneha S', 'Kochi', 19, 'BBA', 45),
    ('Rahul M', 'Palakkad', 22, 'B.Sc Computer Science', 200), ('Aisha N', 'Kannur', 23, 'MCA', 90),
    ('Vishnu T', 'Kollam', 20, 'B.Com', 30), ('Diya J', 'Kottayam', 21, 'BBA', 150),
]


class Command(BaseCommand):
    help = 'Seed demo courses, students, teachers and an admin account.'

    def handle(self, *args, **options):
        admin, created = User.objects.get_or_create(
            username='admin', defaults=dict(first_name='Demo', last_name='Admin', email='admin@demo.college', is_staff=True))
        if created:
            admin.set_password('Admin@123')
            admin.save()

        courses = {}
        for name, fee in COURSES:
            courses[name], _ = Course.objects.get_or_create(coursename=name, defaults={'fees': fee})

        for uname, first, last, course, age, phone, photo in TEACHERS:
            user, created = User.objects.get_or_create(
                username=uname, defaults=dict(first_name=first, last_name=last, email=f'{uname}@demo.college'))
            if created:
                user.set_password('Teacher@123')
                user.save()
            Teacher.objects.get_or_create(user=user, defaults=dict(
                age=age, address='Kerala, India', phone=phone, image=photo, course=courses[course]))

        if not Student.objects.exists():
            today = date.today()
            for name, address, age, course, days_ago in STUDENTS:
                Student.objects.create(studentname=name, address=address, age=age,
                                       joiningdate=today - timedelta(days=days_ago), course=courses[course])

        self.stdout.write(self.style.SUCCESS('Demo data ready: admin/Admin@123, anjali/Teacher@123'))
