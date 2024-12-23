from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('resume/', views.resume_page, name='resume'),
    path('apps/', views.apps_page, name='apps'),
    path('contact/', views.contact_page, name='contact'),
    path("success/", views.success, name="success"),
]