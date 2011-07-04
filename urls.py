from django.conf.urls.defaults import patterns, include, url
from mysite.views import current_datetime
from mysite.books import views



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^time/$', current_datetime),
    (r'^deposit/$', views.deposit_form),
    (r'^deposit-result/$', views.deposit_result),



    




    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
