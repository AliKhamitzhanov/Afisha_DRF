from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializer, UserRegisterSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if not user:
            return Response(data={'message': 'user data are wrong'}, status= status.HTTP_403_FORBIDDEN)
        else:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'key': token.key})


class UserRegisterAPIView(CreateAPIView):
    queryset = User
    serializer_class = UserRegisterSerializer




