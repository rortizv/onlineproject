from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    image = models.ImageField(verbose_name='Image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'
        ordering = ['-created']

    def __str__(self):
        return self.title