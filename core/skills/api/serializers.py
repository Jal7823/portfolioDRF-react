from rest_framework import serializers
from ..models import Library,Language

class SerializersLibrary(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class SerializersLanguage(serializers.ModelSerializer):
    library = SerializersLibrary(many=True)
    class Meta:
        model = Language
        fields = '__all__'