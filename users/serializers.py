from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'phone',
            'password',
            'birthday',
            'gender',
            'email',
            'address',
            'image',
        ]

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone',
            'password',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].validators = []