import pytest
from django.contrib.auth.models import User, Group
from django.test import Client

# from accounts.models import Account
from travel_app.models import City, Plan, Blog, Travel, Travel_Journal


@pytest.fixture
def client():
    return Client()

@pytest.fixture
def city():
    test_city = City.objects.create(
        city_name="Moscow",
        tourist_info_adress = "5454515152",
        places_worth_visiting = "-Petersburskaja Ploshchad",
        restaurants = "Baboska"
    )
    test_city_2 = City.objects.create(
        city_name="NY",
        tourist_info_adress = "5454515152",
        places_worth_visiting = "Mannhatan",
        restaurants = "Panda Express"
    )
    cities = [test_city, test_city_2]
    return test_city

@pytest.fixture
def plan():
    test_plan = Plan.objects.create(
        plan_title="My test plan title",
        task="do the dishes",
        description = "clean them very well"
    )
    plans = [test_plan]
    return test_plan

@pytest.fixture
def blog():
    test_blog = Blog.objects.create(
        #author="My test blog author J.K Rowling",
        post_title="Title post",
        date_of_creation="12-12-2020",
        text="Text to the test post"
    )
    return test_blog

@pytest.fixture
def group():
    group = Group.objects.create(name='travelers')
    return group

@pytest.fixture
def account(group):

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

    )
    account_2.set_password('coderslab')
    account_2.save()
    account_2.groups.add(group)
    test_account = [account_1,account_2]

    return test_account

@pytest.fixture
def travel():
    travel_1 = Travel.objects.create(
        trip_title="Madagaskar",
        city="Antananarywa",
        budget=100
    )
    travel_2 = Travel.objects.create(
        trip_title="Pekin Trip",
        city="Pekin",
        budget=500
    )
    test_travels = [travel_1,travel_2]
    return test_travels

@pytest.fixture
def travel_journal():
    travel_journal_1 = Travel_Journal.objects.create(
        journal_title="New Jork 1",
        places="New Jersey",
    )
    travel_journal_2 = Travel_Journal.objects.create(
        journal_title="NY Trip",
        places="Mannhatan",
    )
    test_travels_journal = [travel_journal_1,travel_journal_2]
    return test_travels_journal