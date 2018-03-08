from django.conf.urls import url
from authentication.views import RegisterView, logout_view

"""
Urls configuration.
1. register/ - registration page, url - register/
2. logout/ - logout page, url - logout/

"""
app_name = 'authentication'
urlpatterns = [
     url(r'register/', RegisterView.as_view(), name='register'),
     url(r'logout/', logout_view, name='logout'),
]
