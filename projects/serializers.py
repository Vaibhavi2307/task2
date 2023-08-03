from .models import Projects
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Projects


