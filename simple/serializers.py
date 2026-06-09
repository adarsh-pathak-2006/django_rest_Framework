from rest_framework import serializers
from .models import database, info

class database_serializer(serializers.ModelSerializer):
    class Meta:
        model=database
        fields='__all__'


class ifo_serializer(serializers.ModelSerializer):
    class Meta:
        model= info
        fields='__all__'