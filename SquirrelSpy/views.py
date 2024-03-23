from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Squirrel, User, Sighting
from .serializers import SquirrelSerializer, UserSerializer, SightingSerializer

class SquirrelViewSet(viewsets.ModelViewSet):
    queryset = Squirrel.objects.all()
    serializer_class = SquirrelSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SightingViewSet(viewsets.ModelViewSet):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer

    @action(detail=False, methods=['get'])
    def by_squirrel(self, request, *args, **kwargs):
        squirrel = request.query_params.get('squirrel')
        sightings = self.queryset.filter(squirrel=squirrel)
        serializer = self.get_serializer(sightings, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_user(self, request, *args, **kwargs):
        user = request.query_params.get('user')
        sightings = self.queryset.filter(user=user)
        serializer = self.get_serializer(sightings, many=True)
        return Response(serializer.data)