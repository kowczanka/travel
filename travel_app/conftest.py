import pytest
from django.contrib.auth.models import User, Group
from django.test import Client

# from accounts.models import Account
from travel_app.models import City, Plan, Blog, Travel, Travel_Journal


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def group():
    group = Group.objects.create(name='travelers')
    return group


@pytest.fixture
def user():
    user = User.objects.create(
        username="JozekPaździoch",
        email="jozekpazdzioch@op.pl"

    )
    user.set_password('coderslab')
    user.save()
    return user


@pytest.fixture
def users(group):
    account_1 = User.objects.create(
        username="JozekPaździoch",
        email="jozekpazdzioch@op.pl",
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
def city(user):
    test_city = City.objects.create(
        city_name="Moscow",
        tourist_info_adress = "5454515152",
        places_worth_visiting = "-Petersburskaja Ploshchad",
        restaurants = "Ruskaja kuchnia",
        author=user
    )
    test_city_2 = City.objects.create(
        city_name="NY",
        tourist_info_adress = "5454515152",
        places_worth_visiting = "Mannhatan",
        restaurants = "Panda Express",
        author=user

    )
    cities = [test_city, test_city_2]
    return cities


@pytest.fixture
def plan(user):
    test_plan = Plan.objects.create(
        plan_title="My test plan title",
        task="do the dishes",
        description="clean them very well",
        author=user
    )
    return test_plan


@pytest.fixture
def blog(user):
    test_blog = Blog.objects.create(
        author=user,
        post_title="Title post",
        text="Text to the test post"
    )
    return test_blog


@pytest.fixture
def travel(user):
    travel_1 = Travel.objects.create(
        trip_title="Madagaskar",
        city="Antananarywa",
        budget=100,
        organizer=user
    )
    travel_2 = Travel.objects.create(
        trip_title="Pekin Trip",
        city="Pekin",
        budget=500,
        organizer=user

    )
    test_travels = [travel_1,travel_2]
    return test_travels


@pytest.fixture
def travel_journal(user):
    travel_journal_1 = Travel_Journal.objects.create(
        journal_title="New Jork 1",
        places="New Jersey",
        author=user
    )
    travel_journal_2 = Travel_Journal.objects.create(
        journal_title="NY Trip",
        places="Mannhatan",
        author=user
    )
    test_travel_journals = [travel_journal_1,travel_journal_2]
    return test_travel_journals