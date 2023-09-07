from django.shortcuts import render
from django.views import View
from .models import Blog
from django.shortcuts import render, get_object_or_404
# Create your views here.
class Home(View):
    @staticmethod
    def get(request):
        queryset = Blog.objects.all()
        return render(request, 'home.html', {'blog': queryset})

class BlogDetail(View):
    @staticmethod
    def get(request, obj_id):
        queryset = Blog.objects.get(id=obj_id)
        return render(request, 'blog-detail.html', {'object': queryset})

class AI(View):
    @staticmethod
    def get(request):
        return render(request, 'artificial-intelligence.html')


class InformationTech(View):
    @staticmethod
    def get(request):
        return render(request, 'informationTech.html')

class Contact(View):
    @staticmethod
    def get(request):
        return render(request, 'contact-us.html')

class About(View):
    @staticmethod
    def get(request):
        return render(request, 'about-us.html')

class Terms(View):
    @staticmethod
    def get(request):
        return render(request, 'terms&conditions.html')

class PrivacyPolicy(View):
    @staticmethod
    def get(request):
        return render(request, 'privacy-policy.html')
