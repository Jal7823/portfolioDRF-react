from rest_framework import serializers
from ..models import Certifications

class SerializersCertifications(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = '__all__'
        