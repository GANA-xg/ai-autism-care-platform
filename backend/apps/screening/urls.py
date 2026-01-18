from rest_framework.routers import DefaultRouter
from .views import ScreeningSessionViewSet

router = DefaultRouter()
router.register(r'screenings', ScreeningSessionViewSet, basename='screenings')

urlpatterns = router.urls