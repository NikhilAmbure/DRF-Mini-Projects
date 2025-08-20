from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password


class SignupAPISerializer(serializers.Serializer):

    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)

    
    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("username already exist.")
        return username
    
    
    def validate_password(self, password):
        if len(password) >= 8:
            if not any(char.isdigit() for char in password):
                raise serializers.ValidationError("Password must contain at least 1 digit.")
            if not any(not char.isalnum() for char in password):
                raise serializers.ValidationError("Password must contain at least 1 special character.")
        else:
            raise serializers.ValidationError("Password must be at least 8 characters.")    
        return password
    

    def validate_email(self, email):
        try:
            validate_email(email)   
        except serializers.ValidationError:
            raise serializers.ValidationError("Invalid email address")
        return email
        
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password doesn't matching.")
        return data    
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        user = User.objects.create(
            username = username,
            password = make_password(validated_data['password']),
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        return user