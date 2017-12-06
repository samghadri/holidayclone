#holidayshare URl
from django.conf.urls import url,include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$',views.MainPage.as_view(),name='index'),
    url(r'^members/',include('members.urls',namespace='members')),
    url(r'^members/',include('django.contrib.auth.urls')),
    url(r'^test/$',views.TestPage.as_view(),name ='test'),
    url(r'^thanks/$',views.Thanks.as_view(),name= 'thanks'),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^groups/',include('groups.urls',namespace='groups')),
    url(r'^api/posts/',include('posts.api.urls', namespace='posts-api'))
]
