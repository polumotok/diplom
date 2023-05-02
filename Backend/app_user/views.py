from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from app_user.Serializers import ProfileSerializer
from app_user.models import Profile


class Profile(APIView):

  def get(self, request):
    product = Profile.objects.all()
    serializer = ProfileSerializer(product, many=True)
    return Response(serializer.data)
  def post(self, request):

    product = Profile.objects.create(avatar=request.data['avatar'],
                                     email=request.data['email'],
                                     fullName=request.data['fullName'],
                                     phone=request.data['phone'],)
    serializer = ProfileSerializer(data=product)
    serializer.is_valid()
    return Response(serializer.data)
