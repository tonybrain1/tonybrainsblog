"""ytechblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings   #ecommercre
from django.conf.urls.static import static   #ecommercre
from django.contrib import admin
from django.urls import include, path      #i learnt how to import include fro python and javascript course
from django.conf.urls import url
from django.contrib.auth import views as auth_views



from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views
from users import views as user_views


urlpatterns = [
     #ecommerc
    path('admin/', admin.site.urls),
    path('about/', profiles_views.about, name='about'), #ecommercre
    path('contact/', contact_views.contact, name='contact'),
    path('checkout/', checkout_views.checkout, name='checkout'),
    #path('post/', include('users.urls', namespace='users'), name='comment'),
    #url(r'^post/', user_views.article_details, name='detail'),
    #path('post/', post_views.post, name='post'),
    path('articles/', profiles_views.articles, name='articles'), #ecommercre

    #path('', include('users.urls', namespace='users'), name='home'),
    #url('users/', include('users.urls'), name='comment'),

    url(r'^accounts/', include('accounts.urls')),
    #url(r'^(?P<slug>[-\w]+)/$', user_views.article_details, name='detail'),

    url(r'^$', user_views.article_list, name="article_list"),
    url(r'^users/', include('users.urls', namespace="users")),
    #url(r'^login/$', user_views.user_login, name="user_login"),
    url(r'^logout/$', user_views.user_logout, name="user_logout"),
    url(r'^register/$', user_views.register, name="register"),

    # Password Reset Url's
    #url(r'^password-reset/$', auth_views.PasswordResetView, name="password_reset"),
    #url(r'^password-reset/done/$', auth_views.PasswordResetDoneView, name="password_reset_done"),
    #url(r'^password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$', auth_views.PasswordResetConfirmView, name="password_reset_confirm"),
    #url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView, name="password_reset_complete"),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^oauth/', include('social_django.urls', namespace="social")),
    url(r'^like/', user_views.like_post, name="like_post"),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

