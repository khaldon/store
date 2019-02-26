from django.views.generic import TemplateView
from braces import views 

class HomePage(TemplateView):
    template_name = 'base_store/index.html'