#importando a biblioteca de 'caminhos' do django
from django.urls import path
#importando as views que criamos da nossa api:
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleAPIView)
router.register(r'planet', PlanetAPIView)
router.register(r'starship', StarshipsAPIView)

urlpatterns = router.urls


