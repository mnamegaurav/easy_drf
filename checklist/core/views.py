from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.views import APIView
# Create your views here.


@api_view(['GET', 'POST'])
def test_api(request):
    return Response({'name': 'Gaurav'})


class TestAPIVIew(APIView):

    def get(self, request, format=None):
        return Response({'name': 'Gaurav from CBV'})