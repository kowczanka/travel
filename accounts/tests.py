import pytest
from django.test import TestCase
from django.urls import reverse


@pytest.mark.django_db
def test_UserView(client, users, group):
    client.force_login(user=users[1])
    response = client.get(reverse('UserView'))
    assert response.status_code == 200
    users_from_view = response.context['objects']
    assert len(users_from_view) == 2
    assert users_from_view[0].username == users[0].username

@pytest.mark.django_db
def test_UserView_not_superuser(client, users, group):
    client.force_login(user=users[0])
    response = client.get(reverse('UserView'))
    assert response.status_code == 403

@pytest.mark.django_db
def test_GroupView(client, group, users):
    client.force_login(user=users[1])
    response = client.get(reverse('GroupView'))
    assert response.status_code == 200
    set = response.context['objects']
    assert len(set) == 1
    assert set[0].name == group.name

@pytest.mark.django_db
def test_GroupView_not_superuser(client, group, users):
    client.force_login(user=users[0])
    response = client.get(reverse('GroupView'))
    assert response.status_code == 403

@pytest.mark.django_db
def test_ChangePermissionView(client, group, users):
    client.force_login(user=users[1])
    response = client.get(reverse("ChangePermissionView", args= (users[0].id,)) )
    assert response.status_code == 200


@pytest.mark.django_db
def test_ChangePermissionView_not_superuser(client, group, users):
    client.force_login(user=users[0])
    response = client.get(reverse("ChangePermissionView", args= (users[0].id,)) )
    assert response.status_code == 403


@pytest.mark.django_db
def test_ChangePermissionViewGroup(client, group, users):
    client.force_login(user=users[1])
    response = client.get(reverse("ChangePermissionViewGroup", args= (group.id,)) )
    assert response.status_code == 200


@pytest.mark.django_db
def test_ChangePermissionViewGroup_not_superuser(client, users):
    client.force_login(users[0])
    response = client.get(reverse("ChangePermissionViewGroup", args= (1,)) )
    assert response.status_code == 403


@pytest.mark.django_db
def test_UserList(client, users):
    client.force_login(user=users[1])
    response = client.get(reverse('UserList'))
    assert response.status_code == 200
    set = response.context['objects']
    assert len(set) == 2
    assert set[0].username == users[0].username

@pytest.mark.django_db
def test_UserList_not_superuser(client, users):
    client.force_login(user=users[0])
    response = client.get(reverse('UserList'))
    assert response.status_code == 403

@pytest.mark.django_db
def test_delete_user_view(client, users):
    client.force_login(user=users[1])
    response = client.get(reverse('delete_user', args=(users[0].pk,)))
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_user_view_not_superuser(client, users):
    client.force_login(user=users[0])
    response = client.get(reverse('delete_user', args=(users[0].pk,)))
    assert response.status_code == 403

@pytest.mark.django_db
def test_user_details_view(client, users):
    client.force_login(user=users[1])
    response = client.get(reverse('user_details', args=(users[0].pk,)))
    assert response.status_code == 200
    assert response.context['objects'].username == users[0].username

@pytest.mark.django_db
def test_user_details_view_not_superuser(client, users):
    client.force_login(user=users[0])
    response = client.get(reverse('user_details', args=(users[0].pk,)))
    assert response.status_code == 403




