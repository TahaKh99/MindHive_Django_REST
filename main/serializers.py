from rest_framework import serializers
from .models import Outlet

class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlet
        fields = ['id', 'name', 'address', 'latitude', 'longitude']
