from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import Operationserializer
from rest_framework import serializers
from enum import Enum


# Create your views here.

class OperationSerializer(serializers.Serializer):
    operation_type = serializers.CharField()
    x = serializers.IntegerField()
    y = serializers.IntegerField()


class Operations(generics.CreateAPIView):
    serializer_class = OperationSerializer

    def post(self, request):
        
            Serializer = self.get_serializer(data=request.data)

            Serializer.is_valid(raise_exception=True)
            operation_type = Serializer.validated_data['operation_type']
            x = Serializer.validated_data['x']
            y = Serializer.validated_data['y']
            result = 0
            if operation_type == 'addition':
                result = x + y

            elif operation_type == 'subtraction':
                result = x - y
            elif operation_type == 'multiplication':
                result = x * y
            data = {
                'slackusername': 'timmy',
                'result': result,
                'operation_type': operation_type,
                
            }
            

            return Response(data)
           