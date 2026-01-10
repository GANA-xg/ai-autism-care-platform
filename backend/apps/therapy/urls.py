from rest_framework.routers import DefaultRouter
from .views import TherapyPlanViewSet

router = DefaultRouter()
router.register(r'therapy-plans', TherapyPlanViewSet, basename='therapy')

urlpatterns = router.urls