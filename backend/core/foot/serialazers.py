from rest_framework import serializers
from .models import Foot


class FootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foot
        fields = ('id', 'name', 'description', 'price', 'picture')
