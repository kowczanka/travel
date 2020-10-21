import pytest
from django.contrib.auth.models import User, Group
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def group():
    group = Group.objects.create(name='travelers')
    return group

@pytest.fixture
def users(group):
    account_1 = User.objects.create(
        username="JozekPaździoch",
        email="jozekpazdzioch@op.pl"
    )
    account_1.set_password('coderslab')
    account_1.save()
    account_1.groups.add(group)

    account_2 = User.objects.create(
        username="Kalinanowak",
        email="kalinanowak@op.pl",
        is_superuser=True
    )
    account_2.set_password('coderslab')
    account_2.save()
    account_2.groups.add(group)
    test_accounts = [account_1,account_2]
    return test_accounts

