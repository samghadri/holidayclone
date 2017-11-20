#members URl
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'members'

urlpatterns =[
    url(r'login/$',auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(), name='logout'),
    url(r'register/$',views.Register.as_view(),name='register'),
]
