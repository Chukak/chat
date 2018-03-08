from django.views.generic import TemplateView


class HomepageView(TemplateView):
    """
    Homepage view.

    Just show homepage template.

    """
    template_name = "homepage/homepage.html"
