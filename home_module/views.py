from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from site_module.models import SiteSetting
from services_module.models import Gallery , Service

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['img_home'] = Gallery.objects.filter(category='main', is_active=True)
        context['services'] = Service.objects.filter(is_active=True)[:3]
        return context


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