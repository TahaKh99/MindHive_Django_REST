from rest_framework import viewsets
from rest_framework_api_key.permissions import HasAPIKey
from .models import Outlet
from .serializers import OutletSerializer

class OutletViewSet(viewsets.ModelViewSet):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    permission_classes = [HasAPIKey]
