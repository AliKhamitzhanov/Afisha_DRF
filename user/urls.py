from django.urls import path
from user.views import UserLoginAPIView, UserRegisterAPIView

urlpatterns = [
    path('login/', UserLoginAPIView.as_view()),
    path('register/', UserRegisterAPIView.as_view())
]