from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView, ListView
from django.http import HttpResponse, JsonResponse
import requests
import json

# Create your views here.
from .forms import WeatherForm
from .models import Weather
from .helpers import api_call


class Index(View):
    def get(self, request):
        return HttpResponse("<h1>This is the index page</h1>")


class ReturnJson(View):
    def get(self, request):
        return JsonResponse({"This is": "the JsonResponse"})


def base_view(request):
    return render(request, "myapp/base.html")


class AboutView(TemplateView):
    template_name = "myapp/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contents"] = [
            {"title": "Its raining", "text": "Nature needs to drink, too."},
            {
                "title": "TemplateView",
                "text": "This page is rendered by a TemplateView",
            },
        ]
        return context


class WeatherFormAddView(FormView):
    model = Weather
    form_class = WeatherForm
    template_name = "myapp/weather-add.html"
    success_url = "/myapp/weather-listing"

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)


# class WeatherListView(ListView):
#     model = Weather
#     context_object_name = "weather_listing"
#     template_name = "myapp/cities-list.html"


class CitiesListView(TemplateView):
    template_name = "myapp/cities-list.html"
    paginate_by = 20
    context_object_name = "cities_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # define api parameters
        url = "https://countries-cities.p.rapidapi.com/location/country/DE/city/list"
        querystring = {"per_page": "20"}
        api_host = "countries-cities.p.rapidapi.com"

        # call helpers.api_call. Get back json
        cities_list_response = api_call(url, api_host, querystring)
        # context["cities_list"] = cities_list_response
        context["cities_list"] = cities_list_response

        return context

class CityDetailView(TemplateView):
    template_name = "myapp/city-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # define api parameters for city details
        url = f"https://countries-cities.p.rapidapi.com/location/city/{kwargs.get('geonameid')}"
        api_host = "countries-cities.p.rapidapi.com"
        # call helpers.api_call. Get back json
        city_detail_response = api_call(url, api_host)

        # define api parameters for city weather
        # lat and lang are required.
        lat = city_detail_response.get("latitude")
        lang = city_detail_response.get("longitude")
        url = f"https://dark-sky.p.rapidapi.com/{lat},{lang}"
        querystring = {"lang": "en", "units": "auto"}
        api_host = "dark-sky.p.rapidapi.com"
        # call helpers.api_call. Get back json
        city_weather_response = api_call(url, api_host, querystring)

        context["city_data"] = city_detail_response
        context["city_weather"] = city_weather_response
        return context
