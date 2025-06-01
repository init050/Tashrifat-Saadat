from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80, verbose_name='نام')
    email = models.EmailField(max_length=254, verbose_name='ایمیل')
    subject = models.CharField(max_length=100, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)


    class Meta:
        verbose_name = "پیام تماس"    
        verbose_name_plural = "پیام‌های تماس"
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    

