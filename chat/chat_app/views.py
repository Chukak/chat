from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class ChatView(TemplateView):
    """
    Chat view.

    Show homepage template.

    """
    template_name = "chat_app/chat.html"

    @login_required(redirect_field_name=None, login_url="/")
    def dispatch(self, request, *args, **kwargs):
        """
        Checks is user is authenticated, return `dispatch` method.
        Otherwise returns redirect to `login_url`.
        """
        return super().dispatch(request, *args, **kwargs)
