from django.urls import path
from . import views


urlpatterns = [
    path('', views.ServiceListView.as_view(), name='servise_page'),
    path('<pk>/', views.ServiceDetailView.as_view(), name = 'service_detail_page'),
]
