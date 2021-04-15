from django.urls import path
from core.views import TestAPIVIew

urlpatterns = [
    path('', TestAPIVIew.as_view())
]
