from django.urls import path
from .views import rasifal_index, RasifalList

urlpatterns = [
    path('', rasifal_index, name='index'),
]
