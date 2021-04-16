from django.urls import path
from core.views import TestAPIVIew, CheckListsAPIView

urlpatterns = [
    path('', TestAPIVIew.as_view()),
    path('api/checklists/', CheckListsAPIView.as_view()),
]
