from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(
        verbose_name="Nombre de usuario",
        max_length=50
    )
    email = models.EmailField(
        verbose_name="Email",
    )
    def __str__(self):
        return self.username
        

