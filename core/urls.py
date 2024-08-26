from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from . import views
from django.conf import settings


app_name = 'core'

urlpatterns = [
    path('', views.front, name='front'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page' : settings.LOGOUT_REDIRECT_URL}, name='logout')
    ]
