from django.urls import path
from Authentication.views import SignupUser, LoginUser,LogoutUser


urlpatterns=[
    path('Signup', SignupUser, name='signup'),
    path('Login', LoginUser, name='login'),
    path('Logout', LogoutUser, name='logout')
]