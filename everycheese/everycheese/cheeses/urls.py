from django.urls import path
from . import views

app_name = "cheeses"

urlpatterns = [
        path(
            route='',
            view=views.CheeseListView.as_view(),
            name='list',
            ),

        path(
            route='add/',
            # this is the coresponding class in views?
            view=views.CheeseCreateView.as_view(),
            name='add'
            ),

        path(
            route='<slug:slug>',
            view=views.CheeseDetailView.as_view(),
            name='detail',
            ),
        ]

# when we add a path. We have to direct something to it in the view


