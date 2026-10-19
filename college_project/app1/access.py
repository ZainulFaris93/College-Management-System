"""Access control for app1 views.

Admins are staff users; teachers are regular users with a Teacher profile.
"""
from functools import wraps

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect

# Accounts created by `python manage.py seed_demo`. In demo mode they can't be
# deleted or edited, so every visitor can still log in with them.
DEMO_USERNAMES = {'admin', 'anjali', 'rohan', 'meera'}


def admin_required(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_page')
        if not request.user.is_staff:
            messages.info(request, "Only the admin can open that page.")
            return redirect('teacher_home')
        return view(request, *args, **kwargs)
    return wrapper


def teacher_required(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_page')
        if request.user.is_staff:
            return redirect('admin_home')
        return view(request, *args, **kwargs)
    return wrapper


def is_protected_demo_user(user):
    return getattr(settings, 'DEMO_MODE', False) and user is not None and user.username in DEMO_USERNAMES
