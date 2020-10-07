from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Prefetch
from .models import Profile, Offers, User
from .serializers import ProfileSerializer, OffserSerializer, UserSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

class ProfileViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        params = self.request.query_params.get(
            'params',
            ''
        )
        return Profile.objects.filter(
            phone_number__icontains = params
        )


class OffersViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Offers.objects.all()
    serializer_class = OffserSerializer
    pagination_class = StandardResultsSetPagination


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination