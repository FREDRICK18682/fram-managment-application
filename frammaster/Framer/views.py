from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer
from django.contrib.auth import authenticate, get_user_model, login
# to fetch the current active user model
User = get_user_model()

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
        password = request.data.get('password')
        
        if not email or not password:
            return Response(
                {"error": "Both Email and Password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 1. Find user by email
            user_obj = User.objects.get(email=email)
            
            # 2. Check if the password matches the hashed password in database
            if user_obj.check_password(password):
                # 3. Log them in and create the session
                login(request, user_obj)
                return Response(
                    {
                        "message": "login successful",
                        "email": user_obj.email,
                        "redirect_url": "/landing/"
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "Invalid email or password."},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        