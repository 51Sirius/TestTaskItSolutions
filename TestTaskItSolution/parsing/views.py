from parsing.models import Advert
from rest_framework import permissions, viewsets, generics
from parsing.serializers import AdvertSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from django.contrib.auth.models import User


class AdvertView(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()

    def get_queryset(self):
        advert_id = self.kwargs.get("advert_id", None)
        if advert_id is not None:
            return Advert.objects.filter(reference_id=advert_id)

        return super().get_queryset()


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
