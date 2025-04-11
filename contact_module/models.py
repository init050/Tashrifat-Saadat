from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80, verbose_name='Name')
    email = models.EmailField(max_length=254, verbose_name='Email')
    subject = models.CharField(max_length=100, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Create At')
    is_read_by_admin = models.BooleanField(verbose_name='Read by admin', default=False)


    class Meta:
        verbose_name = "Contact Message"    
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    

