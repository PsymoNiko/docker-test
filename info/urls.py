from django.urls import path

from .views import PersonAPIView

urlpatterns = [
    path('', PersonAPIView.as_view()),
]