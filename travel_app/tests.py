from django.test import TestCase
import pytest
from django.urls import reverse

from accounts.views import user_details
from travel_app.conftest import plan
from travel_app.models import Travel, City, Travel_Journal, Blog, Plan
from travel_app.views import TravelCreateView


@pytest.mark.django_db
def test_CityCreateView(client, user):
    client.force_login(user=user)
    context = {
        'city_name': "Madrid",
        'tourist_info_adress': "666666",
        'places_worth_visiting': "Palace",
        'restaurants': "Espaniol"
    }
    client.post(reverse('CityCreateView'), context)
    assert City.objects.get(city_name="Madrid")
    assert City.objects.get(places_worth_visiting="Palace")
    assert City.objects.get(restaurants="Espaniol")


@pytest.mark.django_db
def test_CityView(client, city, user):
    client.force_login(user=user)
    response = client.get(reverse('CityView'))
    assert response.status_code == 200

    cities_from_view = response.context['objects']
    assert len(cities_from_view) == 2
    assert cities_from_view[0].city_name == city[0].city_name

@pytest.mark.django_db
def test_CityView_unlogged(client):
    response = client.get(reverse('CityView'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_UpdateCityView(client, city, user):
    client.force_login(user=user)
    context = {
        'city_name': "Moscow2",
        'tourist_info_adress': "5454515152",
        'places_worth_visiting': "-Rynek",
        'restaurants': "Baboska"
    }
    client.post(reverse('UpdateCityView', args=(city[0].pk,)), context)
    assert City.objects.get(city_name=context['city_name'], places_worth_visiting=context['places_worth_visiting'])

# PLAN  #############################################################

@pytest.mark.django_db
def test_PlanCreateView(client, plan, user):
    client.force_login(user=user)
    context = {
        "plan_title": "Trip Vienna Plan",
        "task": "exchange money",
        "description": "buy euros",
        "author": user
    }

    client.post(reverse("PlanCreateView"), context)
    assert Plan.objects.get(plan_title="Trip Vienna Plan")
    assert Plan.objects.get(task="exchange money")
    assert Plan.objects.get(description="buy euros")
    assert Plan.objects.filter(author=user)
    # assert Plan.objects.get(author=user)


@pytest.mark.django_db
def test_PlanView(client, plan, user):
    client.force_login(user=user)
    response = client.get(reverse('PlanView'))
    plan_from_view = response.context['objects']
    assert response.status_code == 200
    assert len(plan_from_view) == 1
    assert plan_from_view[0].plan_title == "My test plan title"
    assert plan_from_view[0].plan_title == plan.plan_title
    assert plan_from_view[0].author == user

def test_PlanView_unlogged(client):
    response = client.get(reverse('PlanView'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_UpdatePlanView(client, plan, user):
    client.force_login(user=user)
    context = {
        "plan_title": "Trip Mexico Plan",
        "task": "buy sombrero",
        "description": "buy pesos",
        "author": user
    }
    client.post(reverse('UpdatePlanView', args=(plan.pk,)), context)
    assert Plan.objects.get(plan_title=context['plan_title'],task=context["task"])

# BLOG  ###################################################

@pytest.mark.django_db
def test_BlogCreateView(client, user):
    client.force_login(user=user)
    context = {
        "author": user,
        "post_title": "Blog trip to Vienna",
        "text": "Post text"
    }

    client.post(reverse("BlogCreateView"), context)
    assert Blog.objects.get(author=user)
    assert Blog.objects.get(post_title="Blog trip to Vienna")
    assert Blog.objects.get(text="Post text")


@pytest.mark.django_db
def test_BlogView(client, blog, user):
    response = client.get(reverse('BlogView'))
    assert response.status_code == 200
    blogs_from_view = response.context['objects']
    assert len(blogs_from_view) == 1
    assert blogs_from_view[0].text == "Text to the test post"
    assert blogs_from_view[0].text == blog.text
    assert blogs_from_view[0].author == user
    assert blogs_from_view[0].post_title == blog.post_title

@pytest.mark.django_db
def test_UpdateBlogView(client, blog, user):
    client.force_login(user=user)
    context = {
        "author": user,
        "post_title": "My first Safari",
        "text": "Safari description"
    }

    client.post(reverse("UpdateBlogView", args=(blog.pk,)), context)
    assert Blog.objects.get(author=user)
    assert Blog.objects.get(post_title="My first Safari")
    assert Blog.objects.get(text=context["text"])

@pytest.mark.django_db
def test_SeeBlog(client, blog, user):
    response = client.get(reverse('SeeBlog', args=(blog.pk,)))
    assert response.status_code == 200
    blogs_from_view = response.context['post']
    assert blogs_from_view.text == "Text to the test post"
    assert blogs_from_view.author == user
    assert blogs_from_view.post_title == blog.post_title

#  TRAVEL  #############################################################################

@pytest.mark.django_db
def test_TravelCreateView(client, user):
    client.force_login(user=user)
    context = {
        "trip_title": "Maledivs",
        "city": "Male",
        "budget": 100000,
        "organizer": user
    }

    client.post(reverse("TravelCreateView"), context)
    assert Travel.objects.get(trip_title=context["trip_title"])
    assert Travel.objects.get(city="Male")
    assert Travel.objects.get(budget=100000)

@pytest.mark.django_db
def test_TravelView(client, travel, user):
    client.force_login(user=user)
    response = client.get(reverse('TravelView'))
    travels_from_view = response.context['objects']

    assert len(travels_from_view) == 2
    assert travels_from_view[0].trip_title == "Madagaskar"
    assert travels_from_view[0].trip_title == travel[0].trip_title
    assert travels_from_view[1].city == "Pekin"
    assert travels_from_view[1].city == travel[1].city
    assert travels_from_view[1].budget == 500
    assert response.status_code == 200

@pytest.mark.django_db
def test_TravelView_unlogged(client):
    response = client.get(reverse('TravelView'))
    assert response.status_code == 302

@pytest.mark.django_db
def test_UpdateTravelView(client, travel, user):
    client.force_login(user=user)
    context = {
        "trip_title": "Warsaw second trip",
        "city": "Warsaw",
        "budget": 50,
        "organizer": user,
    }

    client.post(reverse("UpdateTravelView", args=(travel[0].pk,)), context)
    assert Travel.objects.get(trip_title=context['trip_title'],city=context["city"] )
    assert Travel.objects.get(budget=50)
    # assert Travel.objects.get(organizer=user)


#  JOURNAL #############################################################################

@pytest.mark.django_db
def test_JournalCreateView(client, user):
    client.force_login(user=user)
    context = {
        "journal_title": "Vienna Trip",
        "places": "Schloss",
        "author": user
    }

    client.post(reverse("JournalCreateView"), context)
    assert Travel_Journal.objects.get(journal_title="Vienna Trip")
    assert Travel_Journal.objects.get(places="Schloss")


@pytest.mark.django_db
def test_JournalView(client, travel_journal, user):
    client.force_login(user=user)
    response = client.get(reverse('JournalView'))
    travel_journal = response.context['objects']
    assert response.status_code == 200
    assert len(travel_journal) == 2
    assert travel_journal[0].journal_title == "New Jork 1"
    assert travel_journal[0].places == "New Jersey"
    assert travel_journal[1].journal_title == "NY Trip"
    assert travel_journal[1].places == "Mannhatan"


@pytest.mark.django_db
def test_UpdateJournalView(client, travel_journal, user):
    client.force_login(user=user)
    context = {
        "journal_title": "New Zeland Trip Journal",
        "places": "Hills",
        "author": user
    }
    client.post(reverse('UpdateJournalView', args=(travel_journal[0].pk,)), context)
    assert Travel_Journal.objects.get(journal_title=context['journal_title'], places=context['places'])
