from django.forms import forms as form
from django.forms import ValidationError
from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(form.Form):
    """
    Register form.
    Has 2 attributes - fields:
    1. nickname - nickname user
    2. password - password user

    Also has 1 method:
    1. clean_nickname - validate nickname

    Used django user model.
    """
    nickname = forms.CharField(
        required=True, label='Enter you nickname',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nickname',
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        required=True, label='Enter you password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
            }
        )
    )

    def clean_nickname(self):
        """
        Validate nickname from form. Check, if the nickname exists.

        Return nickname if is valid, otherwise raise ValidationError.
        """
        nickname = self.cleaned_data['nickname']
        if get_user_model().objects.filter(username=nickname).count():
            raise ValidationError('This login already exists.')
        return nickname
