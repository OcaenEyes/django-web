from rest_framework import serializers
from .models import Meizitu

class MzSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meizitu
        fields = '__all__'