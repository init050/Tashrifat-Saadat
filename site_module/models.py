from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='Site Name')
    site_url = models.CharField(max_length=200, verbose_name='Site URL')
    site_logo = models.ImageField(upload_to='images/site_module', blank=True, verbose_name='Site Logo')
    site_favicon = models.ImageField(upload_to='images/site_module', blank=True, verbose_name='Site Favicon')
    site_phone = models.CharField(max_length=50, blank=True, verbose_name='Site Phone')
    site_email = models.EmailField(blank=True, verbose_name='Email')
    site_address = models.TextField(blank=True, verbose_name='Site Address')
    site_copyright = models.TextField(blank=True, verbose_name='Site Copyright')
    is_main_setting = models.BooleanField(default=True, verbose_name='Main Setting')

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings' 


    def __str__(self):
        return self.site_name
    

