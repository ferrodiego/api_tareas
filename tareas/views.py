from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Tarea
from .serializers import TareaSerelializer


class TareaViewset(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerelializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Tarea.objects.filter(usuario = self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(usuario = self.request.user)
    
    