from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from Fashion import settings

admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^register/$', 'outfit.views.register', name='register'),
    url(r'^login_redirect/$', 'outfit.views.login_redirect', name='login_redirect'),
    url(r'^profile/$', 'outfit.views.profile', name='profile'),
    url(r'girly/$', 'outfit.views.girly', name='girly'),
    # url(r'^getall/$', 'outfit.views.getall', name='getall'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # $("#start").show();
    #  Password reset URLS

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),

    # Support old style base36 password reset links; remove in Django 1.7

    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
         name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),




)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)