import jwt
from datetime import datetime, timedelta
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

class AuthenticateView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = authenticate(request, username=email, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=400)

        # Create JWT access token for 60 minutes 
        payload = {
            'id': user.id,
            'expiry': datetime.utcnow() + timedelta(minutes=60),
            'created_at': datetime.utcnow()
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return Response({
            'token': token
        })
