from rest_framework import serializers
from .models import *

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields="__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields="__all__"

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()