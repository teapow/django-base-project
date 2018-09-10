"""Project URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')

    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

    Including another URLconf
        1. Import include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.debug import get_safe_settings
from django.views.generic import TemplateView

admin.site.site_header = f"{settings.PROJECT_NAME} administration"
admin.site.site_title = settings.PROJECT_NAME

settings_view = TemplateView.as_view(
    template_name="admin/settings.html",
    extra_context={
        "title": "Settings",
        "has_permission": True,
        "settings": get_safe_settings(),
        "site_url": "/",
    },
)

urlpatterns = [
    path("admin/settings", settings_view, name="admin-settings"),
    path("admin/", admin.site.urls),
    path("status/", include("watchman.urls")),
]
