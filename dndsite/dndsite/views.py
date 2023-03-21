from django.views.generic import TemplateView
from django.http import HttpResponse
from .utils import get_weather
from .models import WildMagicTable

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
    
class WildMagicView(TemplateView):
    template_name = "wildmagic.html"

    # def get(self, request, *args, **kwargs):
        # import csv
        # with open('C:\\Users\\liisa\\Downloads\\Wild Magic table - Sheet1.csv') as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        #     for line in csv_reader:
        #         a, created = WildMagicTable.objects.get_or_create(
        #             dice_value = line[0],
        #             effect = line[1],
        #             urls = line[2]
        #         )
        #         print(created)
        # return HttpResponse(content="its good")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        magics = WildMagicTable.objects.filter(enabled=True)
        data['magic'] = magics
        return data


    def post(self, request, *args, **kwargs):
        print(request.POST)
        return HttpResponse(content="its good")