from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from site_module.models import SiteSetting

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_module/index.html'



class AboutView(TemplateView):
    template_name = 'home_module/about.html'


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        site_setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
    

def site_header_component(request):
    return render(request, 'site_header_component.html')


def site_footer_component(request):
    return render(request, 'site_footer_component.html')