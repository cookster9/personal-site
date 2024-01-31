from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('contact/', views.contact_page, name='contact'),
    path('about/', views.about_page, name='about'),
    path("success/", views.success, name="success"),
]