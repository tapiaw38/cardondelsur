from rest_framework import serializers
# import models
from .models import Profile, Offers, User, City
# Serializers

class OffserSerializer(serializers.ModelSerializer):
    '''class offer model serializer, includ model profile'''
    user = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    commerce_name = serializers.CharField(source='profile.commerce_name')
    picture = serializers.ImageField(source='profile.picture')
    class Meta:
        model = Offers
        fields = (
            'id',
            'user',
            'first_name',
            'last_name',
            'commerce_name',
            'picture',
            'description',
            'category',
            'image',
            'created',
        )

class CitySerializer(serializers.ModelSerializer):
    '''Clase cities serializars'''

    class Meta:
        model = City
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    '''class profile serializer, includ model user'''
    user = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    is_commerce = serializers.BooleanField(source='user.is_commerce')
    last_name = serializers.CharField(source='user.last_name')
    #related_profiles = OffserSerializer(many=True)
    city = CitySerializer()
    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'first_name',
            'last_name',
            'is_commerce',
            'commerce_name',
            'picture',
            'phone_number',
            'lat',
            'lng',
            'city',
            #'related_profiles',
        )

class UserSerializer(serializers.ModelSerializer):
    '''Modelo para la creacion de perfiles'''
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'is_commerce',
            'profile',
        )

class CitySerializer(serializers.ModelSerializer):
    '''Serializer list all cities'''

    class Meta:
        model = City
        fields = '__all__'
        