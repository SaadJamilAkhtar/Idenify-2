from django.db import models


class Profile(models.Model):
    site_title = models.CharField(max_length=10, default='Idenify')
    name = models.CharField(max_length=255, default="John Doe")
    greeting = models.CharField(max_length=255, default="Hi!")
    main_designation = models.CharField(max_length=255, default="Web Developer")
    about = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to='documents/cv', null=True, blank=True)
    enable_services = models.BooleanField(default=True)
    # services = models.ManyToManyField('Services', blank=True)
    enable_pricing = models.BooleanField(default=True)
    # pricing = models.ManyToManyField('Pricing', blank=True)
    enable_testimonials = models.BooleanField(default=True)
    # testimonials = models.ManyToManyField("Testimonials", blank=True)
    enable_posts = models.BooleanField(default=True)
    # posts = models.ManyToManyField('Posts', blank=True)
    linkedin = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/profile', null=True, blank=True)
    enable_portfolio = models.BooleanField(default=True)
    # portfolio = models.ManyToManyField('Portfolio', blank=True, null=True)


class Settings(models.Model):
    host_list = [('smtp.gmail.com', 'gmail')]
    port_list = [(587, 'gmail')]
    from_email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    to_email = models.EmailField(blank=True, null=True)
    host = models.CharField(max_length=255, choices=host_list, default='smtp.gmail.com')
    port = models.PositiveIntegerField(choices=port_list, default=587)

    class Meta:
        verbose_name_plural = 'Settings'
