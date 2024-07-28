from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from parsing import views

router = routers.DefaultRouter()
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path(
        "adverts/", views.AdvertView.as_view(actions={"get": "list"}), name="adverts"
    ),
    path(
        "adverts/<int:advert_id>/",
        views.AdvertView.as_view(actions={"get": "list"}),
        name="adverts-by-id",
    ),
    path(
        "register/", views.CreateUserView.as_view(), name="create-user"
    ),
]
