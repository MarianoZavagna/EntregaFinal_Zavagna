from django.urls import path

from home import views

app_name='home'
urlpatterns = [
    path('', views.index, name='main'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('policy', views.policy, name='policy'),
    path('terms', views.terms, name='terms'),

]
