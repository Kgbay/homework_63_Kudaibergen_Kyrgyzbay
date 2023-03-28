from django.urls import path

from .views import IndexView
from .views import PostCreateView, PostDetail, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("post/add/", PostCreateView.as_view(), name='post_add'),
    path("posts/<int:pk>/", PostDetail.as_view(), name='post_view'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/confirm_delete/', PostDeleteView.as_view(), name='confirm_delete'),
]