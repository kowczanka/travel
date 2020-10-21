import pytest
from django.contrib.auth.models import User, Group, Permission
from django.test import Client
from travel_app.models import City, Plan, Blog, Travel, Travel_Journal


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def group():
    group = Group.objects.create(name='travelers')
    permissions = Permission.objects.filter(content_type__model="travel_journal")
    group.permissions.set(permissions)
    return group


@pytest.fixture
def users(group):
    account_1 = User.objects.create(
        username="Janinka",
        email="janinka@op.pl",
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

    test_account = [account_1, account_2]
    return test_account


@pytest.fixture
def city(users):
    test_city = City.objects.create(
        city_name="Moscow",
        tourist_info_adress = "5454515152",
        places_worth_visiting = "-Petersburskaja Ploshchad",
        restaurants = "Ruskaja kuchnia",
        author=users[0]
    )
    test_city_2 = City.objects.create(
        city_name="NY",
        tourist_info_adress = "5454515152",
        places_worth_visiting = "Mannhatan",
        restaurants = "Panda Express",
        author=users[0]

    )
    cities = [test_city, test_city_2]
    return cities


@pytest.fixture
def plan(users):
    test_plan = Plan.objects.create(
        plan_title="My test plan title",
        task="do the dishes",
        description="clean them very well",
        author=users[0]
    )
    return test_plan


@pytest.fixture
def blog(users):
    test_blog = Blog.objects.create(
        author=users[0],
        post_title="Title post",
        text="Text to the test post"
    )
    return test_blog


@pytest.fixture
def travel(users):
    travel_1 = Travel.objects.create(
        trip_title="Madagaskar",
        city="Antananarywa",
        budget=100,
        organizer=users[0]
    )
    travel_2 = Travel.objects.create(
        trip_title="Pekin Trip",
        city="Pekin",
        budget=500,
        organizer=users[0]

    )
    test_travels = [travel_1,travel_2]
    return test_travels


@pytest.fixture
def travel_journal(users):
    travel_journal_1 = Travel_Journal.objects.create(
        journal_title="New Jork 1",
        places="New Jersey",
        author=users[0]
    )
    travel_journal_2 = Travel_Journal.objects.create(
        journal_title="NY Trip",
        places="Mannhatan",
        author=users[0]
    )
    test_travel_journals = [travel_journal_1,travel_journal_2]
    return test_travel_journals