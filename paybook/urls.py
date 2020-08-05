from django.urls import path
from . import views

urlpatterns = [
    path("data", views.AboutView.as_view()),
]
