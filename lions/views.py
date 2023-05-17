from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from lions.jwt_serializer import UserModelSerializer

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400) # Bad request
        user = serializer.save()
        token = TokenObtainPairSerializer.get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)
        respone_data = {
            'message': 'register success',
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'token': {
                'access': access_token,
                'refresh': refresh_token,
            },
        }
        return Response(respone_data)
    
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=400) # Bad request
        login(request, user)
        token = TokenObtainPairSerializer.get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)
        response_data = {
            'message': 'login success',
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'token': {
                'access': access_token,
                'refresh': refresh_token,
            },
        }
        return Response(response_data)
    
    def get(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=400) # Bad request
        token = TokenObtainPairSerializer.get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)
        response_data = {
            'message': 'account info',
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'token': {
                'access': access_token,
                'refresh': refresh_token,
            },
        }
        return Response(response_data)
    
    def patch(self, request):
        username = request.data['username']
        password = request.data['password']
        newusername = request.data['newusername']
        newpassword = request.data['newpassword']
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=400) # Bad request
        user.username = newusername
        user.password = newpassword
        user.save()
        token = TokenObtainPairSerializer.get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)
        response_data = {
            'message': 'account info update success',
            'username': user.username,
            'email': user.email,
            'password': user.password,
            'token': {
                'access': access_token,
                'refresh': refresh_token,
            },
        }
        return Response(response_data)