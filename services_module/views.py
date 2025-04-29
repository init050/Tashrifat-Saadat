from django.views.generic import ListView, DetailView
from services_module.models import Service , Gallery , Menu 
# Create your views here.


class ServiceListView(ListView):
    model = Service 
    template_name = 'services_module/service_page.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['services'] = Service.objects.filter(is_active=True)
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
        context['gallery'] = Gallery.objects.filter(category='other', service=self.object, is_active=True)
        context['menus'] = Menu.objects.filter(service=self.object)
        return context
    

    
