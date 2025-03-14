from rest_framework import serializers
from .models import User
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_age(self, value):
        # to check age as a positive integer
        if value < 0:
            raise serializers.ValidationError("Age must be a positive number")
        return value
    
    def validate_name(self, value):
        # name should not be empty
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty") 
        #checks for any digit in name    
        if value.isdigit():
            raise serializers.ValidationError("Name cannot contain numbers")
        #allows name with only letters and spaces
        if not re.fullmatch(r"[A-Za-z\s]+",value):                       
            raise serializers.ValidationError("Name must contain only letters and spaces")
        return value  
    
    def validate_email(self, value):
        # checks if email already exist for creating, allows update for same user
        if self.instance and self.instance.email == value:
            return value
        # for creating new user
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
      