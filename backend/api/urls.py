from django.urls import path, include
from . import views


url_patterns = [
    path("api/", include("api.urls")),
]
