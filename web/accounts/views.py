from django.contrib.auth import get_user_model
from rest_framework import generics as api_view

from web.accounts.serizlizers import CreateUserSerializer

UserModel = get_user_model()


class RegisterView(api_view.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


class LoginView(api_view.CreateAPIView):
    pass


class LogoutView(api_view.CreateAPIView):
    pass