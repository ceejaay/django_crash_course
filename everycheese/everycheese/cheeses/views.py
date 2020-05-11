from django.views.generic import ListView, DetailView, CreateView

from .models import Cheese

class CheeseListView(ListView):
    model = Cheese



class CheeseDetailView(DetailView):
    model = Cheese

# for every view we need a url pattern


class CheeseCreateView(CreateView):
    model = Cheese
    fields = [
            'name',
            'description',
            'firmness',
            'country_of_origin',
            ]

# Then go add the url pattern


