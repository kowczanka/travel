from django.test import TestCase
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_city(client, city):
    response = client.get(reverse('CityView'))
    assert response.status_code == 200
    cities = response.context['objects']
    assert len(cities) == 2
    assert cities[0].city_name == "Moscow"
    assert cities[1].restaurants == "Panda Express"


@pytest.mark.django_db
def test_plan(client, plan):
    response = client.get(reverse('PlanView'))
    assert response.status_code == 200
    plans = response.context['objects']
    assert len(plans) == 1
    assert plans[0].plan_title == "My test plan title"

@pytest.mark.django_db
def test_blog(client, blog):
    response = client.get(reverse('BlogView'))
    assert response.status_code == 200
    blogs = response.context['objects']
    assert len(blogs) == 1
    assert blogs[0].text == "Text to the test post"
    # assert blogs[0].author == Account.username


@pytest.mark.django_db
def test_account(client, account):
    response = client.get(
        reverse('UserView'))
    assert response.status_code == 200
    account = response.context['objects']
    assert len(account) == 2
    assert account[0].username == "JozekPaździoch"

@pytest.mark.django_db
def test_travel(client, travel):
    response = client.get(reverse('TravelView'))
    assert response.status_code == 200
    travels = response.context['objects']
    assert len(travels) == 2
    assert travels[0].trip_title == "Madagaskar"
    assert travels[1].city == "Pekin"
    assert travels[1].budget == 500

@pytest.mark.django_db
def test_travel_journal(client, travel_journal):
    response = client.get(reverse('JournalView'))
    assert response.status_code == 200
    travel_journal = response.context['objects']
    assert len(travel_journal) == 2
    assert travel_journal[0].journal_title == "New Jork 1"
    assert travel_journal[1].places == "Mannhatan"
