import pytest


@pytest.mark.django_db
def test_client_logout_redirect(user_client):
    response = user_client.post('/logout/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_doctor_logout_redirect(user_doctor):
    response = user_doctor.post('/logout/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_superuser_logout_redirect(admin_client):
    response = admin_client.post('/logout/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_service(admin_client, category):
    response = admin_client.post('/add/service/', {'name': 'Service 1', 'category': category, 'price': 10.0})
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_service_notfound(admin_client):
    response = admin_client.post('/delete/service/1/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_delete_service_redirect(admin_client, service):
    response = admin_client.post(f'/delete/service/{service.id}/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_service_notfound(admin_client):
    response = admin_client.post(f'/edit/service/11/0/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_edit_service_success(admin_client, service):
    response = admin_client.post(f'/edit/service/{service.id}/0/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_unknown_page_catch_success(user_client):
    response_client = user_client.get('/unknown-page/')
    assert response_client.status_code == 200


@pytest.mark.django_db
def test_index_page(user_doctor):
    response = user_doctor.get('/')
    assert response.status_code == 200