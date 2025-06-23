from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerelializer


class TareaViewset(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerelializer