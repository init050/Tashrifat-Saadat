from django.db import models

# Create your models here.



class Service(models.Model):


    title = models.CharField(max_length=100, verbose_name='نام دسته‌بندی')
    slug = models.SlugField(unique=True, verbose_name='نامک')
    short_description = models.CharField(max_length=200, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/service_categories', blank=True, verbose_name='تصویر دسته‌بندی')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    min_guests = models.PositiveIntegerField(null=True, blank=True, default=1, verbose_name='حداقل مهمان', help_text='حداقل تعداد مهمان مورد نیاز')
    max_guests = models.PositiveIntegerField(null=True, blank=True, verbose_name='حداکثر مهمان', help_text='حداکثر تعداد مهمان مجاز')


    PRICE_TYPE_CHOICES = [
    ('fixed', 'قیمت ثابت'),   
    ('range', 'بازه قیمت'),
    ('custom', 'قیمت توافقی'),
    ]

    price_type = models.CharField(
        blank=True,
        max_length=20,
        choices=PRICE_TYPE_CHOICES,
        default='fixed',
        verbose_name='نوع قیمت'
    )
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        verbose_name='قیمت پایه',
        help_text='قیمت شروع برای این سرویس'
    )
    price_range_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,    
        verbose_name='حداقل قیمت',
        help_text='حداقل قیمت برای بازه قیمت'
    )
    price_range_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='حداکثر قیمت',
        help_text='حداکثر قیمت برای بازه قیمت'
    )
    

    class Meta:
        verbose_name = 'دسته‌بندی خدمات'
        verbose_name_plural = 'دسته‌بندی‌های خدمات'

    def __str__(self):
        return self.title
    

    

class Menu(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='menus', verbose_name='سرویس')
    title = models.CharField(max_length=200, verbose_name='عنوان منو')

    class Meta:
        verbose_name = 'منو'
        verbose_name_plural = 'منوها'

    def __str__(self) -> str:
        return f"{self.title} - {self.service.title}"




class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='منو')
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'آیتم منو'
        verbose_name_plural = 'آیتم‌های منو'

    def __str__(self) -> str:
        return f"{self.title} ({self.menu.title})"
    


class Gallery(models.Model):

    CATEGORY_CHOICES = [
        ('main', 'گالری اصلی'),
        ('slider', 'تصاویر اسلایدر'),
        ('background', 'تصاویر پس‌زمینه'),
        ('featured', 'تصاویر ویژه'),
        ('other', 'سایر تصاویر'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='main',
        verbose_name='دسته‌بندی تصویر',
        help_text='دسته‌بندی برای فیلتر کردن تصاویر در قالب‌های مختلف'
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='service_images',
        verbose_name='سرویس'
    )
    image = models.ImageField(
        upload_to='images/services/gallery',
        verbose_name='تصویر'
    )

    description = models.TextField(
        blank=True,
        verbose_name='توضیحات تصویر'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')


    class Meta:
        verbose_name = 'تصویر سرویس'
        verbose_name_plural = 'تصاویر سرویس'

    def __str__(self):
        return f"{self.service.title} - {self.image.name}" if self.service else f"تصویر بدون لینک - {self.image.name}"

