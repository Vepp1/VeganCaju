from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


STATUS = ((0, 'Waiting for Approval'), (1, 'Approved'), (2, 'Cancelled'))
FLAVORS = ((0, 'Chocolate'), (1, 'Cocconut'), (2, 'White Chocolate'), (3, 'Pistach'), (4, 'Peanut'))
SIZES = ((0, 'Small - 4 un.'), (1, 'Medium - 6 un.'), (2, 'Large - 10 un.'))


class Order(models.Model):
    flavor = models.IntegerField(choices=FLAVORS, default=0)
    size = models.IntegerField(choices=SIZES, default=0)
    costumer = models.CharField(max_length=80)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    pick_up = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.flavor, self.size
        )