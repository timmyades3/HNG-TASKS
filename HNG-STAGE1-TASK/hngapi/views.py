from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import Profile






@api_view(['GET'])
def profileList(request):
  profiles=Profile.objects.all()
  serializer=ProfileSerializer(profiles, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def profileDetail(request,pk):
  profiles=Profile.objects.get(id=pk)
  serializer=ProfileSerializer(profiles)
  return Response(serializer.data)


@api_view(['POST'])
def profileCreate(request):
  serializer=ProfileSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['POST'])
def profileUpdate(request,pk):
  profile=Profile.objects.get(id=pk)
  serializer=ProfileSerializer(instance=profile, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@api_view(['DELETE'])
def profileDelete(request,pk):
  profile=Profile.objects.get(id=pk)
  profile.delete()
  return Response("successfully deleted")


