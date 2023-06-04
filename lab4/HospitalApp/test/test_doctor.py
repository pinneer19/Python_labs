import pytest
from django.contrib.auth.models import User
from doctor.models import Department, Doctor, Specialization


@pytest.mark.django_db
def test_department_creation():
    department = Department.objects.create(name='Some Department')
    assert department.name == 'Some Department'


@pytest.mark.django_db
def test_specialization_creation(department):
    specialization = Specialization.objects.create(name='Some Specialization', department=department)
    assert specialization.name == 'Some Specialization'
    assert specialization.department == department


@pytest.mark.django_db
def test_doctor_creation(department, specialization):
    user = User.objects.create(username='johndoe')
    doctor = Doctor.objects.create(
        first_name='John',
        last_name='Doe',
        middle_name='Smith',
        login='johndoe',
        password='password123',
        department=department,
        user=user,
    )
    doctor.specialization.add(specialization)
    assert doctor.first_name == 'John'
    assert doctor.last_name == 'Doe'
    assert doctor.middle_name == 'Smith'
    assert doctor.login == 'johndoe'
    assert doctor.password == 'password123'
    assert doctor.department == department
    assert specialization in doctor.specialization.all()
    assert str(doctor) == 'Doe John Smith'
