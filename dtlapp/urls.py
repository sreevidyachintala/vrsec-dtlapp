from django.urls import path
from dtlapp import views
from django.contrib.auth import views as v

urlpatterns=[
path('home/',views.home,name='home'),
path('about/',views.about,name='about'),
path('contact/',views.contact,name='contact'),
#path('login/',views.login,name='login'),
path('register/',views.register,name='register'),
path('dsh/',views.dashboard,name='dsh'),
path('login/',v.LoginView.as_view(template_name='dtlapp/login.html'),name='login'),
path('logout/',v.LogoutView.as_view(template_name='dtlapp/logout.html'),name='logout'),

path('pro/',views.profile,name='profile'),
path('uppro/',views.uppro,name='uppro'),


]


