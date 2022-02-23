from django.urls import path
from .views import HomeView , PostDetailView , PostDeletelView , PostUpdateView , PostCreateView

app_name = 'home'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('post_detail/<slug:post_slug>', PostDetailView.as_view(), name='post_detail'),
    path('post_delete/<int:post_id>', PostDeletelView.as_view(), name='post_delete'),
    path('post_update/<int:post_id>', PostUpdateView.as_view(), name='post_update'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
]
