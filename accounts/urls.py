from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout' ),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='reset_password_form'),
    path('password_reset/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset_done.html'), name='reset_password_done')

]