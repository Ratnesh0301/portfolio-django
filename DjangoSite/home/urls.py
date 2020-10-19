from django.contrib import admin
from django.urls import path, include
from home import views

# Django admin header customization
admin.site.site_header = "Developer Ratnesh"
admin.site.site_title = "Welcome to Ratnesh's Dashboard"
admin.site.index_title = "Welcome to Admin"
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact')
]
