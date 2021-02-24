from django.shortcuts import render

# def index(request):
#     return render(request, "index.html")
from django.views.generic import TemplateView, View

#
# class Index(TemplateView):
#     template_name = "index.html"

class Index(View):
    def get(self, request):
        return render(request, "index.html")