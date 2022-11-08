from rest_framework import serializers
from .models import Operation


class Operationserializer(serializers.ModelSerializer):
  class Meta:
    model = Operation
    fields = '__all__'
  