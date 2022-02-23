from django.urls import path
from .views import *
app_name = 'home'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('post_detail/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post_delete/<int:post_id>/', PostDeletelView.as_view(), name='post_delete'),
    path('post_update/<int:post_id>/', PostUpdateView.as_view(), name='post_update'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_reply/<int:post_id>/<int:comment_id>/', PostAddReplyView.as_view(), name='post_reply'),
    path('post_like/<int:post_id>/', PostLikeView.as_view(), name='post_like'),
]
