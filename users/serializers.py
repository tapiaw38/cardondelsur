from rest_framework import serializers
# import models
from .models import Profile, Offers, User
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

class ProfileSerializer(serializers.ModelSerializer):
    '''class profile serializer, includ model user'''
    user = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    is_commerce = serializers.BooleanField(source='user.is_commerce')
    last_name = serializers.CharField(source='user.last_name')
    #related_profiles = OffserSerializer(many=True)
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
            'lat_city',
            'lng_city',
            'lat',
            'lng',
            #'related_profiles',
        )

class UserSerializer(serializers.ModelSerializer):
    '''Modelo para la creacion de perfiles'''
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'is_commerce',
            'profile',
            ]


