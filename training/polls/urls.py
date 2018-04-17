from django.conf.urls import url
from .views import home, detail, new_question, new_choice

urlpatterns = [
    url(r'home/', home, name='home'),
    url(r'question/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'create_question', new_question, name='new_question'),
    url(r'create_choice/(?P<pk>[0-9]+)/$', new_choice, name='new_choice'),
]
