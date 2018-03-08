from django.conf.urls import url, include
from homepage.views import HomepageView

urlpatterns = [
    # homepage
    url(r'^$', HomepageView.as_view(), name='homepage'),
    # auth
    url(r'auth/', include('authentication.urls')),
    # chat
    url(r'chat/', include('chat_app.urls')),
]
