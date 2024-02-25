from django.urls import path
from . import views

urlpatterns = [
    path('', views.async_leaflet_map, name='leaflet_map'),
    path("success/", views.success, name="success"),
]