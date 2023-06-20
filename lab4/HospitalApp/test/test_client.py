import pytest
from django.contrib.auth.models import User

from client.models import Passport, Client


@pytest.mark.django_db
def test_passport_creation():
    passport = Passport.objects.create(serial='AB', number='1234567')
    assert passport.serial == 'AB'
    assert passport.number == '1234567'


@pytest.mark.django_db
def test_client_creation(passport):
    user = User.objects.create(username='johndoe')
    client = Client.objects.create(
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
    assert client.first_name == 'John'
    assert client.last_name == 'Doe'
    assert client.middle_name == 'Smith'
    assert client.passport == passport
    assert client.user == user
    assert client.password == 'password123'
    assert str(client) == 'Doe J.S.'
