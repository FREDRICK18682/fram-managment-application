from rest_framework import serializers
from .models import UserProfile
#to hash the password in the database
from django.contrib.auth.hashers import make_password
class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = "__all__"
    # to Hash the password before saving it in the database
    def  create(self, validate_data):
        raw_password= validate_data.pop('password', None)
        instance = super().create(validate_data)
        if raw_password is not None:
            instance.password=make_password(raw_password)
            instance.save()
        return instance
    #to handle the hash of an updated password
    def update(self, instance, validate_data):
        raw_password = validate_data.pop('password', None)
        if raw_password is not None:
            instance.password = make_password(raw_password)
        return super().update(instance, validate_data)

