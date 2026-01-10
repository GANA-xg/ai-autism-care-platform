from rest_framework import viewsets
from .models import ProgressLog
from .serializers import ProgressLogSerializer


class ProgressLogViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressLogSerializer

    def get_queryset(self):
        return ProgressLog.objects.filter(
            child__parent=self.request.user
        )