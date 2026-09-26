from django.shortcuts import render


# Create your views here.
def Landing_page(request):
    return render(request, 'land.html')

def signup_view(request):
    return render(request, 'signup.html')