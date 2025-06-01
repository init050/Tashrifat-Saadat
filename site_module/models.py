from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='آدرس سایت')
    site_logo = models.ImageField(upload_to='images/site_module', blank=True, verbose_name='لوگوی سایت')
    site_favicon = models.ImageField(upload_to='images/site_module', blank=True, verbose_name='فاویکون سایت')
    site_phone = models.CharField(max_length=50, blank=True, verbose_name='شماره تماس')
    site_email = models.EmailField(blank=True, verbose_name='ایمیل')
    site_address = models.TextField(blank=True, verbose_name='آدرس')
    site_copyright = models.TextField(blank=True, verbose_name='کپی‌رایت')
    is_main_setting = models.BooleanField(default=True, verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.site_name
    

