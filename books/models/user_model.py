from django.db import models
from django.utils.translation import gettext_lazy as _lazy

# Create your models here.
class Login(models.Model):
    username = models.CharField(
        verbose_name=_lazy("Nombre de usuario"),
        max_length=50
    )
    email = models.EmailField(
        verbose_name=_lazy("Email"),
    )
    def __str__(self):
        return self.username
        

