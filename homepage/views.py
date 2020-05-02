from django.views.generic import TemplateView
from datetime import timedelta


class HomepageView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Context", context)
        context['my_statement'] = "Nice you see you!"

        return context
    
    def say_bye(self):
        return "Goodbye"

    def time_now(self):
        return timedelta.max

    def thing(self):
        return "This is a thing"
