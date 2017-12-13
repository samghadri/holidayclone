from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$',views.PostListApi.as_view(),name='postlist'),
    url(r'^userpost/(?P<username>[\w-]+)/$',views.PostDetailApi.as_view(), name ='detail'),
    url(r'^create/$',views.PostCreateApi.as_view(), name ='create'),

]
