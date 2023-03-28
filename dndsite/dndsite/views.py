from django.views.generic import TemplateView
from django.views.generic import FormView
from django.http import HttpResponse
from .utils import get_weather
from .models import WildMagicTable
from .forms import d100Form
from django.urls import reverse_lazy
import random

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
    
class WildMagicView(FormView):
    template_name = "wildmagic.html"
    form_class = d100Form
    success_url = reverse_lazy("wildmagic")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        variable = self.request.session.get("last_roll")
        magic_roll = None
        try:
            magic_roll = WildMagicTable.objects.get(enabled=True, dice_value = variable)
        except WildMagicTable.DoesNotExist:
            pass
        data['magic'] = magic_roll
        return data

    def form_valid(self, form: d100Form) -> HttpResponse:
        diceroll = random.randint(form.cleaned_data["min_value"], form.cleaned_data["max_value"])
        self.request.session["last_roll"] = diceroll
        self.request.session.modified = True
        return super().form_valid(form)

class UploadFileView(TemplateView):

    def get(self, request, *args, **kwargs):
        import csv
        with open('C:\\Users\\liisa\\Downloads\\Wild Magic table - Sheet1.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                a, created = WildMagicTable.objects.get_or_create(
                    dice_value = line[0],
                    effect = line[1],
                    urls = line[2]
                )
                print(created)
        return HttpResponse(content="its good")