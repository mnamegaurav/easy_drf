from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class TestAPIVIew(APIView):

    def get(self, request, format=None):
        return Response({'name': 'Gaurav from CBV'})