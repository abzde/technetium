from invoice.models import Invoice, Item, InvoiceItem, Profile
from django.contrib import admin

admin.site.register(Invoice)
admin.site.register(Item)
admin.site.register(InvoiceItem)
admin.site.register(Profile)
