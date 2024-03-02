from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("architecture/", include("architecture.urls")),
    path("admin/", admin.site.urls),
]
