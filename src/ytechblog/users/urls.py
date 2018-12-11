from django.urls import path
from django.conf.urls import url

from users import views

app_name = 'users'

#urlpatterns = [
    #path('', views.article_list, name='home'),
    #url(r'^comment/$', views.comment, name='comment'),
#]

urlpatterns = [
    path('', views.article_list, name='article_list'),
    url(r'(?P<id>\d+)/post_edit/$', views.post_edit, name="post_edit"),
    url(r'(?P<id>\d+)/post_delete/$', views.post_delete, name="post_delete"),
    url(r'(?P<id>\d+)/favourite_post/$', views.favourite_post, name="favourite_post"),
    url(r'(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.article_details, name="article_details"),
    url(r'post_create/$', views.post_create, name="post_create"),
    url(r'edit_profile/$', views.edit_profile, name="edit_profile"),
    #url(r'favourites/$', views.post_favourite_list, name="post_favourite_list"),

]

