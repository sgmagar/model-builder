from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SecondHelloViewSet

router = DefaultRouter()
router.register("secondhello", SecondHelloViewSet)

urlpatterns = [path("", include(router.urls))]
