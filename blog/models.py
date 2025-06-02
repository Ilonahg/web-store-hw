from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
