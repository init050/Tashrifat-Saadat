from django.db import models

# Create your models here.



class Service(models.Model):


    title = models.CharField(max_length=100, verbose_name='Category Name')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    short_description = models.CharField(max_length=200, verbose_name='Short Description')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='images/service_categories', blank=True, verbose_name='Category Image')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    min_guests = models.PositiveIntegerField(null=True, blank=True, default=1, verbose_name='Minimum Guests', help_text='Minimum number of guests required')
    max_guests = models.PositiveIntegerField(null=True, blank=True, verbose_name='Maximum Guests', help_text='Maximum number of guests allowed')


    PRICE_TYPE_CHOICES = [
    ('fixed', 'Fixed Price'),   
    ('range', 'Price Range'),
    ('custom', 'Custom Quote'),
    ]

    price_type = models.CharField(
        blank=True,
        max_length=20,
        choices=PRICE_TYPE_CHOICES,
        default='fixed',
        verbose_name='Price Type'
    )
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        verbose_name='Base Price',
        help_text='Starting price for the service'
    )
    price_range_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,    
        verbose_name='Minimum Price',
        help_text='Minimum price for price range type'
    )
    price_range_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='Maximum Price',
        help_text='Maximum price for price range type'
    )
    

    class Meta:
        verbose_name = 'Service Category'
        verbose_name_plural = 'Service Categories'

    def __str__(self):
        return self.title
    

    

class Menu(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='menus')
    title = models.CharField(max_length=200, verbose_name='Menu Title')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self) -> str:
        return f"{self.title} - {self.service.title}"




class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=200, verbose_name='Title')

    class Meta:
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self) -> str:
        return f"{self.title} ({self.menu.title})"
    


class Gallery(models.Model):

    CATEGORY_CHOICES = [
        ('main', 'Main Gallery'),
        ('slider', 'Slider Images'),
        ('background', 'Background Images'),
        ('featured', 'Featured Images'),
        ('other', 'Other Images'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='main',
        verbose_name='Image Category',
        help_text='Category to filter images in different templates'
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='service_images',
        verbose_name='Service'
    )
    image = models.ImageField(
        upload_to='images/services/gallery',
        verbose_name='Image'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Image Description'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')


    class Meta:
        verbose_name = 'Service Image'
        verbose_name_plural = 'Service Images'

    def __str__(self):
        return f"{self.service.title} - {self.image.name}" if self.service else f"Unlinked Image - {self.image.name}"

