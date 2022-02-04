from django.urls import path 
from .views import RegisterAccountView

app_name = 'account'
urlpatterns = [
    path('register_account/', RegisterAccountView.as_view(), name='register_account'),
]
