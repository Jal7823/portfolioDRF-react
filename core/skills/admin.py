from django.contrib import admin
from .models import Library,Language

admin.site.register([Library,Language])