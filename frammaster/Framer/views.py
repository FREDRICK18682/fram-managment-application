from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer


# Create your views here.
def Landing_page(request):
    return render(request, 'land.html')

def signup_view(request):
    return render(request, 'signup.html')

#creaing an Api to save the data in the Database
@api_view(['POST'])
def create_user_api(request):
    serializer = UserProfileSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()#save the data in the database
        return Response({"Message":"User was regested succesfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)