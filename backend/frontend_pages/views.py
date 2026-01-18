from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from apps.children.models import Child
from apps.screening.models import ScreeningSession
from apps.therapy.models import TherapyPlan
from apps.progress.models import ProgressLog

from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 1️⃣ Check if username exists
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(
                request,
                "auth/login.html",
                {"error": "Username does not exist"}
            )

        # 2️⃣ Username exists → check password
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(
                request,
                "auth/login.html",
                {"error": "Incorrect password"}
            )

        # 3️⃣ Successful login
        login(request, user)

        if user.role == "parent":
            return redirect("parent-dashboard")
        elif user.role == "clinician":
            return redirect("clinician-dashboard")
        else:
            return redirect("/admin/")

    return render(request, "auth/login.html")
    


@login_required
def parent_dashboard(request):
    children = Child.objects.filter(parent=request.user)

    child_data = []
    for child in children:
        last_screening = (
            ScreeningSession.objects
            .filter(child=child)
            .order_by("-created_at")
            .first()
        )

        therapy_count = TherapyPlan.objects.filter(child=child).count()

        child_data.append({
            "child": child,
            "risk": last_screening.risk_level if last_screening else "Not screened",
            "therapy_count": therapy_count,
        })

    return render(
        request,
        "parent/dashboard.html",
        {"child_data": child_data}
    )

@login_required
def parent_screening(request):
    children = Child.objects.filter(parent=request.user)

    if request.method == "POST":
        child_id = request.POST.get("child_id")
        child = Child.objects.get(id=child_id, parent=request.user)

        answers = [
            request.POST.get("q1") == "on",
            request.POST.get("q2") == "on",
            request.POST.get("q3") == "on",
        ]

        score = sum(answers)

        if score <= 1:
            risk = "low"
        elif score == 2:
            risk = "medium"
        else:
            risk = "high"

        ScreeningSession.objects.create(
            child=child,
            age_in_months=24,
            total_score=score,
            risk_level=risk,
        )

        return redirect("parent-dashboard")

    return render(
        request,
        "parent/screening.html",
        {"children": children}
    )


@login_required
def clinician_dashboard(request):
    children = Child.objects.all()

    recent_screenings = ScreeningSession.objects.order_by("-created_at")[:5]
    progress_count = ProgressLog.objects.count()

    return render(
        request,
        "clinician/dashboard.html",
        {
            "children": children,
            "recent_screenings": recent_screenings,
            "progress_count": progress_count,
        }
    )


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
