from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import CheckList
# Create your views here.


class TestAPIVIew(APIView):

    def get(self, request, format=None):
        return Response({'name': 'Gaurav from CBV'})


class CheckListsAPIView(APIView):

    def get(self, request, format=None):
        data = CheckList.objects.all()
        return Response(data)