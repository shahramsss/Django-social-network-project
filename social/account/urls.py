from django.urls import path 
from .views import * 

app_name = 'account'
urlpatterns = [
    path('register_account/', RegisterAccountView.as_view(), name='register_account'),
    path('login_account/', UserLoginView.as_view(), name='login_account'),
    path('logout_account/', UserLogoutView.as_view(), name='logout_account'),
    path('profile_account/', UserProfileView.as_view(), name='profile_account'),
    path('reset_password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('password_reset_done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', UserPasswordResetConfrimView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('users/', Users.as_view(), name='users'),
    path('user_posts/<int:user_id>', UsersPosts.as_view(), name='user_posts'),
    path('user_follow/<int:user_id>', UserFollow.as_view(), name='user_follow'),
    path('user_unfollow/<int:user_id>', UserUnFollow.as_view(), name='user_unfollow'),
    path('edit_user/', EditUserView.as_view(), name='edit_user'),
]
