from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
    
    def __str__(self):
        return self.titulo + self.contenido
    
