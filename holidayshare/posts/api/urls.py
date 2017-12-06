from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$',views.PostListApi.as_view(),name='postlist'),
]
