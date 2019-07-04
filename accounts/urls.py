from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('validate_username/', views.validate_username, name='validate_username'),
]
