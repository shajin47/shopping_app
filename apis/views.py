from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from .serializers import UsersSerializer
# Create your views here.

@api_view(['POST'])
def register(request):
    try:
        return Response(request.data)
    except: 
        return Response("there is an error!")  
    
@api_view(["GET"])
def getUser(requset):
    try:
        users_details = Users.objects.all()
        serializer  = UsersSerializer(users_details, many = True)
        return Response(serializer.data)
    except:
        return Response("error!")