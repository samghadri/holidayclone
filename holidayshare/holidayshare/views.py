from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'

class Thanks(TemplateView):
    template_name = 'thanks.html'

class MainPage(TemplateView):
    template_name = 'index.html'
