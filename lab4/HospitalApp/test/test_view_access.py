import pytest

from client.models import Client


@pytest.mark.django_db
def test_client_main_view_redirected(user_client):
    response = user_client.get('/main/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_doctor_main_view_redirected(user_doctor):
    response = user_doctor.get('/main/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_superuser_main_view_allowed(admin_client: Client):
    response = admin_client.get('/main/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_doctor_view_forbidden(user_client):
    response = user_client.get('/doctor/info/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_superuser_doctor_success(admin_client):
    response = admin_client.get('/doctor/info/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_doctor_view_allowed(user_doctor):
    response = user_doctor.get('/doctor/info/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_view_allowed(user_client):
    response = user_client.get('/client/info/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_order_view_forbidden(user_doctor):
    response = user_doctor.get('/client/order/')
    assert response.status_code == 403
