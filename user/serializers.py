from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')

class EditUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number','profile_image')
        
    def validate_phone_number(self, value):
        if value == None or value == "":
            return value
        if not (value.startswith('۰۹') or value.startswith('09')):
            raise serializers.ValidationError("شماره موبایل شما باید با ۰۹ شروع شود")
        if len(value) != 11 :
            raise serializers.ValidationError("شماره موبایل 11 رقمی است")
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        
        instance.save()
        return instance