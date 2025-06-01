from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class CustomAdminSite(admin.AdminSite):
    site_header = settings.ADMIN_SITE_HEADER
    site_title = settings.ADMIN_SITE_TITLE
    index_title = settings.ADMIN_INDEX_TITLE

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        # Customize the order of apps
        app_ordering = {
            'home_module': 1,
            'services_module': 2,
            'contact_module': 3,
            'site_module': 4,
        }
        app_list.sort(key=lambda x: app_ordering.get(x['app_label'], 999))
        return app_list

admin_site = CustomAdminSite(name='admin')

# Register your models here
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin) 