#importa as tabelas models que criamos
from .models import *
#importa os serializers que criamos
from .serializers import *
#importar a classe de configuração da API
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status


class PeopleAPIView(APIView):
    def delete(self, request, peopleId = ''):
        # try:
            #busca o usuario com o id
            peopleFound = People.objects.get(id=peopleId)
            peopleFound.delete() #deleta o usuario com o id encontrado
            return Response(status=status.HTTP_200_OK, data="People successfully deleted!")
        # except People.DoesNotExist:
            # return Response(status=status.HTTP_404_NOT_FOUND,data="People not Found!")
    def put(self, request, peopleId = ''):
        #o people já existente no banco:
        peopleFound = People.objects.get(id=peopleId)
        #o people com os dados novos
        peopleJson = request.data #coletando o json que veio do cliente
        #update
        peopleSerialized = PeopleSerializer(peopleFound, data=peopleJson)
        peopleSerialized.is_valid(raise_exception=True)
        peopleSerialized.save()
        return Response(status=status.HTTP_200_OK, data=peopleSerialized.data)

    def post(self, request):
        #recebe o json que veio do cliente
        peopleJson = request.data
        #converter json em python!
        peopleSerialized = PeopleSerializer(data=peopleJson)
        #verifica se conversão é válida!
        peopleSerialized.is_valid(raise_exception=True)
        #salva no banco de dados (insert into people ...)
        peopleSerialized.save()
        return Response(status=status.HTTP_201_CREATED, data=peopleSerialized.data)

    def get(self, request, peopleId = ''):

        if peopleId == '': #se estiver vazio, pega tudo!

            if 'height' in request.GET:
                peopleFound = People.objects.filter(height__gt=request.GET['height'])
                peopleSerialized = PeopleSerializer(peopleFound, many=True)
                return Response(peopleSerialized.data)
            #primeiro vamos fazer um select all do banco:
            peopleFound = People.objects.all() #select *from people;
            #agora pegamos os dados em python e mandamos p/ json
            peopleSerialized = PeopleSerializer(peopleFound, many=True)
            #manda a resposta para quem chamou a API:
            #Response(data="ok")
            return Response(peopleSerialized.data)
        else: #coletando people do id solicitado!
            try:
                peopleFound = People.objects.get(id=peopleId)
                #select *from people where id = peopleId
                peopleSerialized = PeopleSerializer(peopleFound, many=False)
                return Response(peopleSerialized.data)            
            except People.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data='People Not Found!')

class PlanetAPIView(APIView):
    def get(self, request, planetId =''):
        if planetId == '':
            #primeiro vamos fazer um select all do banco:
            planetFound = Planet.objects.all() #select *from Planet;
            #agora pegamos os dados em python e mandamos p/ json
            planetSerialized = PlanetSerializer(planetFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(planetSerialized.data)
        else: 
            try:
                planetFound = Planet.objects.get(id=planetId)
                planetSerialized = PlanetSerializer(planetFound, many=False)
                return Response(planetSerialized.data)            
            except Planet.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data='Planet Not Found!')
        
        
class StarshipsAPIView(APIView):
    def get(self, request, starshipId = ''):
        if starshipId == '':
            #primeiro vamos fazer um select all do banco:
            starshipsFound = Starships.objects.all() #select *from Starships;
            #agora pegamos os dados em python e mandamos p/ json
            starshipsSerialized = StarshipsSerializer(starshipsFound, many=True)
            #manda a resposta para quem chamou a API:
            return Response(starshipsSerialized.data)
        else:
            try:
                starshipsFound = Starships.objects.get(id=starshipId)
                starshipsSerialized = StarshipsSerializer(starshipsFound, many=False)            
                return Response(starshipsSerialized.data)
            except Starships.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND,  data='Starship Not Found!')

        
