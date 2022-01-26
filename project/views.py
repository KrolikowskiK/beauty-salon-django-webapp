from django.shortcuts import redirect, render


def intro_view(request):
    if hasattr(request.user, "employee"):
        return redirect("appointment-list")
    return render(request, "intro.html")
