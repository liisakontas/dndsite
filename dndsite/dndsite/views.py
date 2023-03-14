from django.views.generic import TemplateView
from .utils import get_weather

class HomeView(TemplateView):
    template_name = "home.html"

class WeatherView(TemplateView):
    template_name = "weather.html"

    def get(self, request, *args, **kwargs):
        anyvariable = super().get(request, *args, **kwargs)
        get_weather('nov', 29)
        #TODO handle str input for date
        return anyvariable
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['test'] = 'crisps'
        return data