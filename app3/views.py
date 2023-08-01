from django.shortcuts import render

# Create your views here.

def jspiders(request):
    return render(request,'jspiders.html')