import pytest
from pytest_django.asserts import assertContains
from django.urls import reverse
from django.contrib.sessions.middleware \
        import SessionMiddleware

from django.test import RequestFactory

from everycheese.users.models import User
from ..models import Cheese
from ..views import (
        CheeseCreateView,
        CheeseListView,
        CheeseDetailView,
        )

from .factories import CheeseFactory
pytestmark = pytest.mark.django_db



def test_good_cheese_list_view_expanded(rf):
    # Shortened test
    # get the request
    request = rf.get(reverse("cheeses:list"))
    # use the request to get the response
    response = CheeseListView.as_view()(request)
    # Test that the response is valid
    assertContains(response, "Cheese List")

    # determine the url
    # url = reverse("cheeses:list")
    # rf is pytest shortcut to django.test.RequestFactory
    # We generate a request as if from a user accessing
    # the cheeses list view
    # request = rf.get(url)
    # Call as_view() to make a callable object
    # callable_obj is anagalous to a functional-based view
    # callable_obj = CheeseListView.as_view()
    # Pass in the request into the callable_obj() to get an HTTP response served up by Django
    # response = callable_obj(request)
    # Test that the HTTP response has "Cheese List" in the HTML and has a 200 response code.

    # assertContains(response, "Cheese List")


def test_good_cheese_detail_view(rf):
    # Order some cheese from the CheeseFactory
    cheese = CheeseFactory()
    # make a request for our new cheese
    url = reverse("cheeses:detail",
            kwargs={"slug": cheese.slug})
    request = rf.get(url)
    # use the request to get the response
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug=cheese.slug)
    # test that the response is valid
    assertContains(response, cheese.name)



def test_good_cheese_create_view(rf, admin_user):
    # Order some cheese from the Cheese factory
    cheese = CheeseFactory()
    # make a request for our new cheese
    request = rf.get(reverse("cheeses:add"))
    # Add an authenticated user.
    request.user = admin_user
    # Use the request to get the response
    response = CheeseCreateView.as_view()(request)
    # Test that the response is valid
    assert response.status_code == 200


def test_cheese_list_contains_2_cheeses(rf):
    # create a couple of cheeses.
    cheese1 = CheeseFactory()
    cheese2 = CheeseFactory()
    # create a request and then a response
    # for a list of cheeses
    request = rf.get(reverse('cheeses:list'))
    print(request)
    response = CheeseListView.as_view()(request)
    # assert that the response contains both cheese names in the template.

    assertContains(response, cheese1.name)
    assertContains(response, cheese2.name)

def test_detail_contains_cheese_data(rf):
    cheese = CheeseFactory()
    url = reverse("cheeses:detail",
            kwargs={"slug": cheese.slug}
            )
    request = rf.get(url)
    callable_obj = CheeseDetailView.as_view()
    # print("this is the callable object.", callable_obj)
    response = callable_obj(request, slug=cheese.slug)
    assertContains(response, cheese.name)
    assertContains(response, cheese.get_firmness_display())
    assertContains(response, cheese.country_of_origin.name)



def test_cheese_create_form_valid(rf, admin_user):
    # submit the cheese add form.
    form_data = {
            "name": "Paski Sir",
            "description": "A salty, hard cheese",
            "firmness": Cheese.Firmness.HARD,
            }

    request = rf.post(reverse("cheeses:add"), form_data)
    request.user = admin_user
    response = CheeseCreateView.as_view()(request)
    # get the cheese based on the name
    cheese = Cheese.objects.get(name="Paski Sir")
    assert cheese.description == "A salty, hard cheese"
    assert cheese.firmness == Cheese.Firmness.HARD
    assert cheese.creator == admin_user


