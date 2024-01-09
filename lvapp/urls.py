from django.contrib import admin
from django.urls import include, path
urlpatterns = [
path("homepage/", include("lvapps.urls")),
path("admin/", admin.site.urls),
]

