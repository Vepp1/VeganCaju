from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError


STATUS = ((0, 'Waiting for Approval'), (1, 'Approved'),
        (2, 'Cancelled'))
FLAVORS = ((0, 'Chocolate'), (1, 'Cocconut'), (2, 'White Chocolate'),
        (3, 'Pistach'), (4, 'Peanut'))
SIZES = ((0, 'S - 4 un. / $5,00'), (1, 'M - 6 un. / $7,00'),
        (2, 'L - 10 un. / $10,00'))


def validate_date(value):
    if value < (timezone.now() + timedelta(days = 4)).date():
        raise ValidationError(
            ('value is not a future datetime'),
            params = {'value': value},
             )

class Order(models.Model):
    flavor = models.IntegerField(choices = FLAVORS, default = 0)
    size = models.IntegerField(choices = SIZES, default = 0)
    costumer = models.CharField(max_length = 80)
    created_on = models.DateTimeField(auto_now_add = True)
    pick_up = models.DateField(validators = [validate_date])
    status = models.IntegerField(choices = STATUS, default = 0)


    class Meta:
        ordering = ['created_on']


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.flavor, self.size
         )

