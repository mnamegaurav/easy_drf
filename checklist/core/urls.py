from django.urls import path
from core.views import test_api, TestAPIVIew

urlpatterns = [
    path('', test_api),
    path('class/', TestAPIVIew.as_view())
]
