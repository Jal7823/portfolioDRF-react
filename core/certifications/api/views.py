from rest_framework import viewsets,status

from .serializers import SerializersCertifications
from ..models import Certifications

class ViewSetCertifications(viewsets.ModelViewSet):
    queryset = Certifications.objects.all()
    serializer_class = SerializersCertifications