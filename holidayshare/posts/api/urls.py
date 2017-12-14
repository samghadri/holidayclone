from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$',views.PostListApi.as_view(),name='postlist'),
    url(r'^create/$',views.PostCreateApi.as_view(), name ='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.PostDetailApi.as_view(),name='single'),


]
