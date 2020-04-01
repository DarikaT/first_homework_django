from django.db import models

class Images(models.Model):
    title = models.CharField(blank = True, max_length=40)
    image = models.ImageField(upload_to='media') 
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галареи'