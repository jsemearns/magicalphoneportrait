from django.conf.urls import include, url
from django.contrib import admin

from magic.views import HomeView, MessageFacebookUser

urlpatterns = [
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^message/$', MessageFacebookUser.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
