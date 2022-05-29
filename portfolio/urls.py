#  hello/urls.py

from django.shortcuts import render
from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('education', views.education_page_view, name='education'),
    path('projects', views.projects_page_view, name='projects'),
    path('skills', views.skills_page_view, name='skills'),
    path('bachelors', views.bachelors_page_view, name='bachelors'),
    path('blog', views.blog_page_view, name='blog'),
    path('quizz', views.quizz, name='quizz'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
    path('web', views.web_page_view, name='web'),
    path('contact', views.contact_page_view, name='contact'),
    path('add_teacher', views.add_Teacher_view, name='add_teacher'),
    path('add_language', views.add_Language_view, name='add_teacher')
]