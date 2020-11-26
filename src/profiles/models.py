from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

# Create your models here.


class UserNet(AbstractUser):
    """модель юзера"""

    GENDER = {
        ('male', 'male'),
        ('female', 'female')
    }

    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    avatar = models.ImageField(upload_to="user/avatar/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.URLField(blank=True, null=True, max_length=500)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=8, default='male')
    technology = models.ManyToManyField('Technology', related_name='users')


class Technology(models.Model):
    """ скилы """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
