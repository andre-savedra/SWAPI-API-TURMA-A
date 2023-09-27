#importa as tabelas models que criamos
from .models import *
#importa os serializers que criamos
from .serializers import *
#importar a classe de configuração da API
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


import django_filters

class PeopleFilter(django_filters.FilterSet):
   name = django_filters.CharFilter(lookup_expr='icontains')
   height = django_filters.NumberFilter(lookup_expr='gte')

   class Meta:
      model = People
      fields = ['name', 'height']

class PeopleAPIView(ModelViewSet):
   queryset = People.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = PeopleSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend] #usa a lib django-filter
   filterset_class = PeopleFilter

class PlanetAPIView(ModelViewSet):
   queryset = Planet.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = PlanetSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend] #usa a lib django-filter
   filterset_fields = ['name', 'climate', 'diameter']
        
class StarshipsAPIView(ModelViewSet):
   queryset = Starships.objects.all() #informa p/ a lib qual as consultas a serem feitas
   serializer_class = StarshipsSerializer #informa o serializer
   filter_backends = [DjangoFilterBackend] #usa a lib django-filter
   filterset_fields = ['name', 'model', 'passengers']
