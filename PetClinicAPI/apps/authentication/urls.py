from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from PetClinicAPI.apps.authentication.views import UserViewSet, MyTokenObtainPairView

router = SimpleRouter()
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
