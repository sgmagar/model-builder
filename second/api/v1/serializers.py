from rest_framework import serializers
from second.models import SecondHello


class SecondHelloSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondHello
        fields = "__all__"
