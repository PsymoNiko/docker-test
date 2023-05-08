from rest_framework import generics, status, response, permissions

from .serializers import PersonSerializers
from .models import Person


class PersonAPIView(generics.ListCreateAPIView):
    serializer_class = PersonSerializers
    permission_classes = [permissions.AllowAny]
    queryset = Person.objects.all()
