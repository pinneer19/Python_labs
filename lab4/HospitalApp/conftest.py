import pytest
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from django.test import Client as DjangoClient
from service.models import ServiceCategory, Service
from doctor.models import Specialization, Department, Doctor
from client.models import Passport, Client


@pytest.fixture(scope="function")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        # create any initial data required
        pass


@pytest.fixture
def passport():
    return Passport.objects.create(serial='AB', number='1234567')


@pytest.fixture
def client_group():
    try:
        group = Group.objects.get(name='client')
    except Group.DoesNotExist:
        group = Group.objects.create(name='client')
        content_type = ContentType.objects.get_for_model(Client)

        permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.set(permissions)
    return group


@pytest.fixture
def doctor_group():
    try:
        group = Group.objects.get(name='doctor')
    except Group.DoesNotExist:
        group = Group.objects.create(name='doctor')
        content_type = ContentType.objects.get_for_model(Doctor)
        permissions = Permission.objects.filter(content_type=content_type)
        group.permissions.set(permissions)
    return group


@pytest.fixture
def client(passport, client_group):
    user = User.objects.create(username='johndoe')
    client_group.user_set.add(user)

    return Client.objects.create(
        first_name='John',
        last_name='Doe',
        middle_name='Smith',
        passport=passport,
        user=user,
        password='password123',
        birthday='2000-01-01',
        address='123 Main St',
        phone='+375 (12) 345-67-89',
    )


@pytest.fixture
def django_client(django_db_setup):
    django_client = DjangoClient()
    return django_client


@pytest.fixture
def user_client(django_db_setup, client: Client):
    django_client = DjangoClient()
    django_client.force_login(client.user)
    return django_client


@pytest.fixture
def department():
    return Department.objects.create(name='Some Department')


@pytest.fixture
def specialization(department):
    return Specialization.objects.create(name='Some Specialization', department=department)


@pytest.fixture
def doctor(department, specialization, doctor_group):
    user = User.objects.create(username='johndoe')
    doctor_group.user_set.add(user)
    return Doctor.objects.create(
        first_name='John',
        last_name='Doe',
        middle_name='Smith',
        login='johndoe',
        password='password123',
        department=department,
        user=user,
    )


@pytest.fixture
def user_doctor(doctor):
    django_client = DjangoClient()
    django_client.force_login(doctor.user)
    return django_client


@pytest.fixture
def admin_client(django_db_setup):
    client = DjangoClient()
    user = User.objects.create_user(
        username='test_admin',
        email='test_user@example.com',
        password='password',
        is_superuser=True
    )
    client.force_login(user)
    return client


@pytest.fixture
def category():
    return ServiceCategory.objects.create(name='Test Department')


@pytest.fixture
def service(category):
    return Service.objects.create(name='Test Service', category=category, price=100)
