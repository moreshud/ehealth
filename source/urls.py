"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from core import views
from core.patient import views as patient_views
from core.doctor import views as doctor_views

patient_urlpatterns = [
    path("", patient_views.dashboard, name="dashboard"),
    # path("profile", patient_views.profile, name="profile"),
]

doctor_urlpatterns = [
    path("", doctor_views.dashboard, name="dashboard")
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sign-in/", auth_views.LoginView.as_view(template_name="sign-in.html")),
    path("sign-out/", auth_views.LogoutView.as_view(next_page="/")),
    path("sign-up/", views.sign_up),
    
    path("", views.home),
    path("patient/", include((patient_urlpatterns, "patient"))),
    path("doctor/", include((doctor_urlpatterns, "doctor"))),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
