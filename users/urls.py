from rest_framework import routers
from django.urls import path, re_path, include
from .viewsets import ProfileViewset, OffersViewset, UserViewset

router = routers.SimpleRouter()
router.register('listProfiles', ProfileViewset)
router.register('listOffers', OffersViewset)
router.register('createUser', UserViewset)

urlpatterns = [
    
]+ router.urls