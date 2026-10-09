from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.hashers import make_password

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        # REMOVE 'username' from this list if it does not exist on your model!
        # Only include fields that actually exist in models.py for UserProfile
        fields = ['id', 'email', 'password'] 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = UserProfile(**validated_data)
        if password is not None:
            instance.password = make_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password is not None:
            instance.password = make_password(password)
            instance.save()
        return instance