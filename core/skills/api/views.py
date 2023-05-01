from rest_framework import viewsets,status

from .serializers import SerializersLibrary,SerializersLanguage
from ..models import Language,Library

class ViewSetLibrary(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = SerializersLibrary

class ViewSetLanguage(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = SerializersLanguage