#holidayshare URl
from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$',views.MainPage.as_view(),name='index'),
    url(r'members/',include('members.urls',namespace='members')),
    url(r'members/',include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
]
