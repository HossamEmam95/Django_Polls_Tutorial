from django.conf.urls import url
from .views import home, detail


urlpatterns = [
    url(r'home', home, name="home"),
    url(r'question/(?P<pk>[0-9]+)/$',detail, name='detail' )
]