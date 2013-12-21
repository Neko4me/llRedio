from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'llRedio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'llRedioWeb.views.IndexHandler', name='IndexHandler'),
    url(r'^type/$', 'llRedioWeb.views.TypeHandler', name='TypeHandler'),
    url(r'^search/$', 'llRedioWeb.views.SearchHandler', name='SearchHandler'),
)
