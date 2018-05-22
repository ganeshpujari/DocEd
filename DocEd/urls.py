from django.conf.urls import include, url
from django.contrib import admin
from base.views import index
from DocEd import settings
from django.views.static import serve


urlpatterns = [
    # Examples:
    # url(r'^$', 'DocEd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sign-up/', index),
    url(r'^assets/(?P<path>.*)$', serve,{'document_root': settings.ASSETS}),
]
