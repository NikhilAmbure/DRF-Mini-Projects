from django.shortcuts import render
from rest_framework.response import Response
from .serializers import SignupAPISerializer
from rest_framework.views import APIView


class SignUpAPI(APIView):

    def post(self, request):
        serializer = SignupAPISerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "status": True,
                "message": "User registered successfully!"
            })
        
        return Response({
            "status": False, 
            "message": serializer.errors
        })