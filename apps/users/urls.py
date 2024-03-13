from django.urls import path, include
from rest_framework import routers
from usuers.views import userView

router = routers.DefaultRouter()
router.register(r'usuario', userView.index, 'usuario')

urlpatterns = [
    path("api/v1/", include(router.urls))
]