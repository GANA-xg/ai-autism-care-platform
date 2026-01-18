from django.urls import path
from .views import (
    login_view,
    parent_dashboard,
    parent_screening,
    clinician_dashboard,
    logout_view,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    path("parent/dashboard/", parent_dashboard, name="parent-dashboard"),
    path("parent/screening/", parent_screening, name="parent-screening"),

    path("clinician/dashboard/", clinician_dashboard, name="clinician-dashboard"),
]
