from rest_framework import serializers
from .models import Youone

class YouoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youone
        fields = "__all__"

        # fields = ('id','imgUrl','textNum','imgAuther','textContent','mon','day')
