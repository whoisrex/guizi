from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

__author__ = 'whoisrex'


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    00Vh0xCHYftqt2lHzuvjluQdIoeUyDml
    00Vh0xCHYftqt2lHzuvjluQdIoeUyDml
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


@admin_required
@ensure_csrf_cookie
def home(request):
    return render(request, "management/index.html")
