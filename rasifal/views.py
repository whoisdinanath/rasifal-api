from django.shortcuts import render, HttpResponse
from .rasifal import get_rasifal
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
import datetime
from django.utils import timezone

from .models import Rasifal, Rasifal_Desc
from .serializers import RasifalSerializer
# Create your views here.


def rasifal_index(request):
    return HttpResponse("This is a home page of rasifal api. Please visit /api/rasifal/ to get rasifal")


def fetch_rasifal():
    #print("Hello world.............................")
    query = Rasifal.objects.all()
    rasi_query = Rasifal_Desc.objects.all()

    if not rasi_query.filter(date=timezone.now().date()).exists():
        rasifal = get_rasifal()
        for title, desc in rasifal.items():
            if not query.filter(title=title).exists():
                rasi = Rasifal.objects.create(title=title)

            rasi = Rasifal.objects.get(title=title)
            Rasifal_Desc.objects.create(rasi=rasi,
                                        description=desc.split('\n')[0])


class RasifalList(ListAPIView):
    #queryset = Rasifal_Desc.objects.filter(date=timezone.now().date())
    serializer_class = RasifalSerializer

    def get(self, request):
        fetch_rasifal()
        return self.list(request)

    def get_queryset(self):
        return Rasifal_Desc.objects.filter(date=timezone.now().date())
