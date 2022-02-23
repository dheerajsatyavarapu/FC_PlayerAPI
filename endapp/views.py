from django.shortcuts import render
from django.db.models import Avg
from rest_framework.views import APIView
from .models import Player
from rest_framework import status,response
from rest_framework.response import Response
# Create your views here.
class CountryStats(APIView):
    def get(self,request):
        result = (Player.objects.values('nationality').annotate(avg_overall=Avg('overall')).order_by())
        country_stats = {}
        for i in list(result):
            country_stats[i['nationality']] = i['avg_overall']
        
        print(country_stats)
        return Response({'country_stats':country_stats},status=status.HTTP_200_OK)

class PlayerStats(APIView):
    def get(self,request):
        result = Player.objects.filter(overall__gt=90).order_by()
        result = list(result)
        print(result)
        player_stats = {}
        for i in result:
            player_stats[i.name] = i.overall
        print(player_stats)
        return Response({'player_stats':player_stats},status=status.HTTP_200_OK)