from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer
from django.contrib.auth import authenticate, get_user_model


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

# creating an APi to Logging 
class logingAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password  = request.data.get('password')
        #check if the Email and password fired have beening filled
        if not email or not password:
            return Response(
                {"error":"Both Email and Password are rquired"},
                status=status.HTTP_400_BAD_REQUEST
            )
         # to safly check if the email and password exist  and if not it gracefully catches the error and set the user to none
        try:
            user_obj = user.object.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except user.DoesNotExist:
            user=None

        if user is not None:
            #the Authentication was successfull
            return Response(
                {
                    "message":"login successful",
                    "email":user.email,
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalide email and password."},
                status=status.HTTP_401_UNAUTHORIZED
            )