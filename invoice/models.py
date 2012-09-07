import string
import random

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __unicode__(self):
        return "<Item n:%s p:%s>" % (self.name, self.price)

class InvoiceItem(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    count = models.DecimalField(decimal_places=2, max_digits=10)
    cost = models.DecimalField(decimal_places=2, max_digits=10, blank=True,
            null=True)

    def __unicode__(self):
        return "<InvoiceItem i:%s #:%s c:%s>" %(self.item, self.count, self.cost)
    
    def save(self, *a, **kw):
        self.cost = float(self.item.price) * float(self.count)
        super(InvoiceItem, self).save(*a, **kw)

class Invoice(models.Model):
    user = models.ForeignKey(User)
    bill_to = models.TextField()
    items = models.ManyToManyField(InvoiceItem)
    date = models.DateTimeField()
    total = models.DecimalField(decimal_places=2, max_digits=10, blank=True,
            null=True)
    secret_key = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return "<Invoice b:%s d:%s t:%s>" % (self.bill_to, self.date, self.total)

    def save(self, *a, **kw):
        if self.secret_key is None:
            self.secret_key = ''.join([random.choice(
                    string.digits+string.ascii_uppercase+string.ascii_lowercase
                ) for x in range(0,30)])
        super(Invoice, self).save(*a, **kw)
        self.total = sum([item.cost for item in self.items.all()])
        super(Invoice, self).save(*a, **kw)

class Profile(models.Model):
    user = models.OneToOneField(User)
    info = models.TextField()

