from rest_framework import viewsets
from .models import ScreeningSession
from .serializers import ScreeningSessionSerializer


class ScreeningSessionViewSet(viewsets.ModelViewSet):
    serializer_class = ScreeningSessionSerializer

    def get_queryset(self):
        return ScreeningSession.objects.filter(
            child__parent=self.request.user
        )