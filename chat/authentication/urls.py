from django.conf.urls import url
from .views import RegisterView, LoginView, logout_view

"""
Urls configuration.
1. register/ - registration page, url - register/
2. login/ - login page, url - login/
3. logout/ - logout page, url - logout/

"""
app_name = "authentication"
urlpatterns = [
     url(r'register/$', RegisterView.as_view(), name="register"),
     url(r'login/$', LoginView.as_view(), name="login"),
     url(r'logout/$', logout_view, name="logout"),
]
