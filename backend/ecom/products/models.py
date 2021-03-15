from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"), null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    price = models.FloatField(_("price"))
    quantity = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name