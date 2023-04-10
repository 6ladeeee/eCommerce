from django.urls import path
from .views import login, SignUpView, logout_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('accounts/profile/', login, name='profile'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]