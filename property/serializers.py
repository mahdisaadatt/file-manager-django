from rest_framework import serializers
from .models import *
from user.models import UserProfile


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name')


class HomeSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer()
    attributes = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Home
        fields = ('id', 'title', 'description', 'address', 'attributes', 'rooms', 'homeType', 'cover', 'price', 'pricePerMeter', 'meterage', 'mortgage', 'rent', 'author', 'createdAt', 'score')

class CarSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer()
    attributes = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Car
        fields = ('id', 'title', 'description', 'address', 'cover', 'price', 'attributes', 'author', 'createdAt', 'score')

class OtherSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer()
    # attributes = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Other
        fields = ('id', 'title', 'description', 'address', 'cover', 'price', 'author', 'createdAt', 'score')


class HomeDetailSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer()
    attributes = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Home
        fields = '__all__'

class CarDetailSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer()
    attributes = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Car
        fields = '__all__'

class OtherDetailSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()
    # attributes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Other
        fields = '__all__'