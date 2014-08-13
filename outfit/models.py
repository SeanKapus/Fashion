from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class User(AbstractUser):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    # imageClient = models.ImageField(upload_to='profile_pics/')

    # unicode is supposed to return a unicode string return u"{}".format(self.username)
    def __unicode__(self):
        return self.username


# Need to fix the indentation here
TYPE_CHOICES = (
                ('T', 'Tops'),
                ('B', 'Bottoms'),
                ('S', 'Shoes'),
                ('A', 'Accessories'),
                ('H', 'Headwear'),
)


class Clothes(models.Model):
    name = models.CharField(max_length=50)
    # 'type' is a reserved python keyword and may cause some funky issues
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    description = models.CharField(max_length=200, blank=True)
    client = models.ForeignKey(User)
    image = models.ImageField(upload_to='cloths/')

    def __unicode__(self):
        return self.name


