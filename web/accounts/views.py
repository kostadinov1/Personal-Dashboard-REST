from django.contrib.auth import get_user_model
from rest_framework import generics as api_view
from rest_framework import views as rest_views
from rest_framework.authtoken import views as auth_views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from web.accounts.serizlizers import CreateUserSerializer


UserModel = get_user_model()


class RegisterView(api_view.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


class LoginView(auth_views.ObtainAuthToken):
    pass


class LogoutView(rest_views.APIView):

    @staticmethod
    def __perform_logout(request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'message': 'User Has Logged Out!'})

    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)
