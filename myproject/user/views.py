from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

from rest_framework.authtoken.models import Token


class LoginView(APIView):
    def post(self,req):
        username = req.data.get('username')
        password = req.data.get('password')

        user = authenticate(req, username=username,password=password)
        if user is not None:
            #Login successful
            return Response({"detail":"Login Successful"}, status=status.HTTP_200_OK)
        else:
            #login failed
            return Response({"detail":"Ivalid credentials"},status=status.HTTP_400_BAD_REQUEST)


class SignUpAPIview(APIView):
    def post(self, req):
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            res = {
                'user': serializer.data,
                'token': token.key,
            }
            return Response(res, status=201)
        return Response(serializer.errors, status=400)