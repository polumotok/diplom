from rest_framework import serializers
from django.contrib.auth.models import User
from app_user.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']

class AvatarSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ["url"]
    def get_url(self):
        return self.obj.avatar
