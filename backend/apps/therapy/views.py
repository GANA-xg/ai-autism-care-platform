from rest_framework import viewsets
from .models import TherapyPlan
from .serializers import TherapyPlanSerializer


class TherapyPlanViewSet(viewsets.ModelViewSet):
    serializer_class = TherapyPlanSerializer

    def get_queryset(self):
        return TherapyPlan.objects.filter(
            child__parent=self.request.user
        )