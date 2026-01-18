from rest_framework import viewsets
from .models import Child
from .serializers import ChildSerializer


class ChildViewSet(viewsets.ModelViewSet):
    serializer_class = ChildSerializer

    def get_queryset(self):
        user = self.request.user
        return Child.objects.filter(parent=user)

    def perform_create(self, serializer):
        serializer.save(parent=self.request.user)