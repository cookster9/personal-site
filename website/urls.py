from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('contact/', views.contact_page, name='contact'),
    path('resume/', views.resume_page, name='resume'),
    path("success/", views.success, name="success"),
]