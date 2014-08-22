from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

# Probably want to also put null=True where you have blank=True on fields
# Also probably want to reformat this file, some whitespaces and syntax issues
class User(AbstractUser):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    gender = models.CharField( max_length=1, choices=GENDER_CHOICES)
    # imageClient = models.ImageField(upload_to='profile_pics/')

    def __unicode__(self):
        return self.username


TYPE_CHOICES = (
                ('T', 'Tops'),
                ('B', 'Bottoms'),
                ('S', 'Shoes'),
                ('A', 'Accessories'),
                ('H', 'Headwear'),
)


class Clothes(models.Model):
    name = models.CharField(max_length=50)
    # type is a reserved keyword in python
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    description = models.CharField(max_length=200, blank=True)
    client = models.ForeignKey(User)
    image = models.ImageField(upload_to='clothes/')

    def __unicode__(self):
        return self.name

class Favorites(models.Model):
    outfit = models.ManyToManyField(Clothes)
    # should name this fields user, with a related_name=favs
    favs =models.ForeignKey(User)



