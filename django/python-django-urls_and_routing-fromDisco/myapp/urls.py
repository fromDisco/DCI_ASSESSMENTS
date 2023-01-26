from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("json/", views.ReturnJson.as_view(), name="return-json"),
    path("base/", views.base_view, name="base"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("cities-list/", views.CitiesListView.as_view(), name="cities-list"),
    path(
        "city-detail/<int:geonameid>",
        views.CityDetailView.as_view(),
        name="city-detail",
    ),
]
