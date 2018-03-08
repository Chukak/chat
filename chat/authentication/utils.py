"""
Utils for authentication here.

"""


def check_user_auth(user):
    """
    Return `True` if not user is authenticated, otherwise `False`.

    """
    return True if not user.is_authenticated() else False
