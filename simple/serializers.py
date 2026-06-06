from rest_framework import serializers
from .models import database

class database_serializer(serializers.Serializer):
    name=serializers.CharField()
    desc=serializers.CharField()


