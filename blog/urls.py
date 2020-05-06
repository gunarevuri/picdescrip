from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    PostLikedRedirectView,
    CommentCreateView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/like/', PostLikedRedirectView.as_view(), name='post-like'),
    path('post/<int:pk>/comment/', views.comment, name='post-comment'),
    path('post/<int:pk>/new/', CommentCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]
