#importa as tabelas models que criamos
from .models import *
#importa os serializers que criamos
from .serializers import *
#importar a classe de configuração da API
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class PeopleAPIView(APIView):
    def get(self, request):
        #primeiro vamos fazer um select all do banco:
        peopleFound = People.objects.all() #select *from people;
        #agora pegamos os dados em python e mandamos p/ json
        peopleSerialized = PeopleSerializer(peopleFound, many=True)
        #manda a resposta para quem chamou a API:
        #Response(data="ok")
        return Response(peopleSerialized.data)
        

class PlanetAPIView(APIView):
    def get(self, id =''):
        if id == '':
            #primeiro vamos fazer um select all do banco:
            planetFound = Planet.objects.all() #select *from Planet;
            #agora pegamos os dados em python e mandamos p/ json
            planetSerialized = PlanetSerializer(planetFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(planetSerialized.data)
        else: 
            planetFound = Planet.objects.get(id=id)
            planetSerialized = PlanetSerializer(planetFound, many=True)
            return Response(planetSerialized.data)
        
        
class StarshipsAPIView(APIView):
    def get(self, request):
        #primeiro vamos fazer um select all do banco:
        starshipsFound = Starships.objects.all() #select *from Starships;
        #agora pegamos os dados em python e mandamos p/ json
        starshipsSerialized = StarshipsSerializer(starshipsFound, many=True)
        #manda a resposta para quem chamou a API:
        Response(starshipsSerialized.data)
        
        
