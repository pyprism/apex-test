from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pilotlog import views

router = DefaultRouter()
router.register(r"pilotlog", views.PilotLogViewSet, basename="pilotlog")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
