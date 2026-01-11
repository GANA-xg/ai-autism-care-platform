from rest_framework.routers import DefaultRouter
from .views import ChildViewSet

router = DefaultRouter()
router.register(r'children', ChildViewSet, basename='children')

urlpatterns = router.urls