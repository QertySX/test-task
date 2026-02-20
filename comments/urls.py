from django.urls import path

from .views import CommentsListAPIView

urlpatterns = [
    path("comments/", CommentsListAPIView.as_view()),
]
