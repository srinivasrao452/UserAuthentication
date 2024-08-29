
from django.urls import path

from users import views as user_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', user_views.home_view, name='home_page'),

    path('contact/', user_views.contact_view, name='contact_page'),

    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login_page'),

    path('logout/', user_views.logout_view, name='logout_page'),

    path('register/', user_views.register_view, name='register_page'),
]
