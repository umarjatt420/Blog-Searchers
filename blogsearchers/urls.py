"""blogsearchers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import Home
from blogs.views import BlogDetail
from blogs.views import AI
from blogs.views import InformationTech
from blogs.views import Contact
from blogs.views import About
from blogs.views import Terms
from blogs.views import PrivacyPolicy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    path('blogs/<int:obj_id>', BlogDetail.as_view()),
    path('contact-us/', Contact.as_view()),
    path('about-us/', About.as_view()),
    path('terms&conditions/', Terms.as_view()),
    path('privacy-policy/', PrivacyPolicy.as_view()),
    path('category/artificial-intelligence/', AI.as_view()),
    path('category/information-technology/', InformationTech.as_view()),
    path('category/computer-network/', AI.as_view()),
    path('category/programming/', AI.as_view()),
    path('category/operating-systems/', AI.as_view()),
    path('category/robotics/', AI.as_view()),
    path('category/quantum-computing/', AI.as_view()),
    path('category/data-science/', AI.as_view()),
    path('category/automation/', AI.as_view()),
    path('category/virtual-reality/', AI.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
