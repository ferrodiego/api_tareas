from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewset


router = DefaultRouter()
router.register(r'tareas', TareaViewset)


urlpatterns = [
    path('', include(router.urls)),
]
