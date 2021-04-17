from rest_framework import serializers

from core.models import CheckList

class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'