from django.conf.urls import url
from .views import ChatView

"""
Urls configuration.
1. '' - char page, url - chat/

"""
app_name = "chat"
urlpatterns = [
    url(r'', ChatView.as_view(), name="chat"),
]
