from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from app_user.Serializers import ProfileSerializer, AvatarSerializer, PasswordSerializer
from app_user.models import Profile


class ProfileView(APIView):

  def get(self, request):
    product = Profile.objects.get(user_id=request.user.id)
    serializer = ProfileSerializer(product)
    return Response(serializer.data)
  def post(self, request):
    product = Profile.objects.update(
                                     email=request.data['email'],
                                     fullName=request.data['fullName'],
                                     phone=request.data['phone'],)
    serializer = ProfileSerializer(data=product)
    serializer.is_valid()
    return Response(serializer.data)

class Avatar(APIView):

  def post(self, request):

    avatar = Profile.objects.get_or_create(avatar=request.data['avatar'],
                                     )
    serializer = AvatarSerializer(data=avatar)
    serializer.is_valid()
    return Response(serializer.data)

class PasswordView(GenericAPIView):
  queryset = User.objects.all()
  serializer_class = ProfileSerializer
  permission_classes = [IsAuthenticated]
  def post(self, request):
    user = User.objects.get(pk=request.user.pk)
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      if not user.check_password(serializer.data.get('passwordCurrent')):
        return Response(data={'passwordCurrent': 'Не верный пароль'}, status=status.HTTP_400_BAD_REQUEST)
      elif serializer.data.get('password') != serializer.data.get('passwordReply'):
        return Response(data={'password': 'Не верный пароль'}, status=status.HTTP_400_BAD_REQUEST)
      user.set_password(serializer.data.get('password'))
      user.save()
      return Response(data={'password': serializer.data.get('password')}, status=status.HTTP_200_OK)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)