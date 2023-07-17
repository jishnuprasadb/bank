
from django.urls import path

from bank_app import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('new_page/',views.new_page,name="new_page"),
    path('register/',views.register,name='register')
]