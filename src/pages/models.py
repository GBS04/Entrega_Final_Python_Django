from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Page.objects.exclude(pk=self.pk).filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
