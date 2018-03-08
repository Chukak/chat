from django.shortcuts import redirect, HttpResponseRedirect
from django.views.generic import FormView
from django.forms import ValidationError
from .forms import RegisterForm, LoginForm
from .utils import check_user_auth
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout, get_user_model


class TestCookie:
    """
    Test cookie object.

    Check if cookie worked.

    Return `True` if is worked, otherwise `False`.
    """
    def test_cookie(self, request):
        if request.session.test_cookie_worked():
            return True
        else:
            return False


class LoginView(FormView, TestCookie):
    """
    Login view.
    Has 3 attributes:
    1. form_class - form class, which is used.
    2. success_url - url, which is redirected in case of success.
    3. template_name - path to template for this view.

    Also, has 3 override methods:
    1. get - when get method is used.
    2. post - when post method is used.
    3. form_valid - check valid form or not
    """
    template_name = "authentication/login.html"
    form_class = LoginForm
    success_url = "/chat/"

    @method_decorator(user_passes_test(check_user_auth, login_url="/", redirect_field_name=None))
    def dispatch(self, request, *args, **kwargs):
        """
        Override dispatch method with decorator. Check is use is authenticated,
        redirect to `login_url`. Otherwise returns `dispatch` method.

        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Set test cookie, and returns `get` method.

        """
        request.session.set_test_cookie()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Checks is cookie is worked. If cookie is worked, validate form.
        Returns `form_valid` method if worked, otherwise `form_invalid` method.

        If cookie not worked, returns `form_invalid` method.

        """
        form = self.get_form()
        if self.test_cookie(request):
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Authenticate and login new user.
        If user is authenticated, returns redirect to success url.

        Otherwise, add error in form and returns `form_invalid` method.

        """
        user_auth = authenticate(self.request, username=form.cleaned_data["nickname"],
                                 password=form.cleaned_data["password"])
        if user_auth is not None:
            login(self.request, user_auth)
            # Redirect chat/
            return redirect(self.get_success_url())
        else:
            # Add error in form for field nickname
            form.add_error("nickname", ValidationError("Invalid Login or password."))
            return self.form_invalid(form)


class RegisterView(FormView, TestCookie):
    """
    Registration view.
    Has 3 attributes:
    1. form_class - form class, which is used.
    2. success_url - url, which is redirected in case of success.
    3. template_name - path to template for this view.

    Also, has 3 override methods:
    1. get - when get method is used.
    2. post - when post method is used.
    3. form_valid - check valid form or not

    """
    form_class = RegisterForm
    success_url = "/chat/"
    template_name = "authentication/register.html"

    @method_decorator(user_passes_test(check_user_auth, login_url="/", redirect_field_name=None))
    def dispatch(self, request, *args, **kwargs):
        """
        Override dispatch method with decorator. Check is use is authenticated,
        redirect to `login_url`. Otherwise returns `dispatch` method.

        """
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Set test cookie, and returns `get` method.

        """
        request.session.set_test_cookie()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Checks is cookie is worked. If cookie is worked, validate form.
        Returns `form_valid` method if worked, otherwise `form_invalid` method.

        If cookie not worked, returns `form_invalid` method.

        """
        form = self.get_form()
        if self.test_cookie(request):
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        Create user object with form. Authenticate and login new user.
        If user is authenticated, returns redirect to success url.

        Otherwise, returns `form_invalid` method.

        """
        user = get_user_model().objects.create_user(username=form.cleaned_data["nickname"],
                                                    password=form.cleaned_data["password"])
        user.save()
        # Authenticate this user
        user_auth = authenticate(username=form.cleaned_data["nickname"],
                                 password=form.cleaned_data["password"])
        if user_auth is not None:
            # Login this user
            login(self.request, user_auth)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


def logout_view(request):
    """
    Logout function.

    Returns redirect to homepage.

    """
    logout(request)
    return HttpResponseRedirect("/")
