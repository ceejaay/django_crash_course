from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        )

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Cheese

class CheeseListView(ListView):
    model = Cheese



class CheeseDetailView(DetailView):
    model = Cheese

# for every view we need a url pattern


class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = [
            'name',
            'description',
            'firmness',
            'country_of_origin',
            ]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

# Then go add the url pattern


class CheeseUpdateView(LoginRequiredMixin, UpdateView):
    model = Cheese
    fields = [
            'name',
            'description',
            'firmness',
            'country_of_origin',
            ]
    action = "Update"
