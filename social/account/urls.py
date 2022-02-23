from django.urls import path 
from .views import RegisterAccountView , UserLoginView , UserLogoutView , UserProfileView ,UserPasswordResetView 

app_name = 'account'
urlpatterns = [
    path('register_account/', RegisterAccountView.as_view(), name='register_account'),
    path('login_account/', UserLoginView.as_view(), name='login_account'),
    path('logout_account/', UserLogoutView.as_view(), name='logout_account'),
    path('profile_account/', UserProfileView.as_view(), name='profile_account'),
    path('reset_password/', UserPasswordResetView.as_view(), name='reset_password'),
]
