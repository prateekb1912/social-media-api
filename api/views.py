from datetime import datetime, timedelta

import jwt
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile


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
            'exp': datetime.utcnow() + timedelta(minutes=60),
            'iat': datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return Response({
            'token': token
        })

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        current_user = UserProfile.objects.get(user=request.user)

        user_to_follow = get_object_or_404(UserProfile, id=id)

        if user_to_follow.user not in current_user.followings.all():
            current_user.followings.add(user_to_follow.user)
            user_to_follow.followers.add(current_user)

            current_user.save()
            user_to_follow.save()

        return Response({
            'status': 'success'
        })

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        current_user = UserProfile.objects.get(user=request.user)

        user_to_follow = get_object_or_404(UserProfile, id=id)

        if user_to_follow.user in current_user.followings.all():
            current_user.followings.remove(user_to_follow.user)
            user_to_follow.followers.remove(current_user)

            current_user.save()
            user_to_follow.save()

        return Response({
            'status': 'success'
        })
