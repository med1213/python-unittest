
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LiveDataViewSet, index

router = DefaultRouter()

router.register("api/v1/live", LiveDataViewSet, basename="live")


urlpatterns = [
    path("live/", index,),
] + router.urls