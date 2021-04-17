from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import CheckList

from core.serializers import CheckListSerializer
# Create your views here.


class TestAPIVIew(APIView):

    def get(self, request, format=None):
        return Response({'name': 'Gaurav from CBV'})


class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer

    def get(self, request, format=None):
        data = CheckList.objects.all()

        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data

        return Response(serialized_data)