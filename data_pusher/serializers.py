from rest_framework import serializers
from django.contrib.auth import get_user_model
from data_pusher.models import Destination


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'has_website']


class DestinationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['user', 'url', 'http_method', 'headers']