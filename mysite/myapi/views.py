from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
from django.http import HttpResponse
from .models import Hero
import json 

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    
def show_list(request):
    show = Hero.objects.all().order_by('id')
    list1 = []
    for x in show:
        dict1 = {"id":x.id,"name": x.name,"alias": x.alias}
        list1.append(dict1)
    json_list = json.dumps(list1)
    return HttpResponse(json_list)
        