from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
# Create your views here.

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
        context["contents"] = [{"title": "Its raining", "text": "Nature needs to drink, too."}, {"title": "TemplateView", "text": "This page is rendered by a TemplateView"}] 
        return context
    