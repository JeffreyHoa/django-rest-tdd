
# Create your models here.

from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    '''
        User 对 AbstractUser 仅仅是继承，没有进行任何的扩展。
        所以，若我们继承AbstractUser，可以获得User的所有特性。
        进一步，覆盖默认的 AUTH_USER_MODEL in settings.py
    '''
    pass


from django.db import models
class Movie(models.Model):
    title        = models.CharField(max_length=255)
    genre        = models.CharField(max_length=255)
    year         = models.CharField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
