from django.urls import path

from api.views import PostView, DetailView, UpdateView, DeleteView

urlpatterns = [
    path("posts/", PostView.as_view()),
    path("posts/<int:pk>/", DetailView.as_view()),
    path("posts/<int:pk>/update/", UpdateView.as_view()),
    path("posts/<int:pk>/delete/", DeleteView.as_view()),
]