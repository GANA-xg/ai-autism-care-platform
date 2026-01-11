from rest_framework.routers import DefaultRouter
from .views import ProgressLogViewSet

router = DefaultRouter()
router.register(r'progress', ProgressLogViewSet, basename='progress')

urlpatterns = router.urls