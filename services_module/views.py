from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from services_module.models import Service 
# Create your views here.


class ServiceListView(ListView):
    model = Service 
    template_name = 'services_module/service_page.html'

    def get_context_data(self):
        context = super(ServiceListView, self).get_context_data()
        return context
    
    def get_queryset(self):
        query = super(ServiceListView, self).get_queryset()
        query = query.filter(is_active=True)
        return query
    


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services_module/service_detail_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.object
        context['gallery'] = service.service_images.filter(is_active=True)
        context['menus'] = self.object.menus.prefetch_related('items')
        return context
    

    
