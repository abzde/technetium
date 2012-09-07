from django import forms
from django.forms.formsets import formset_factory
import datetime

class InvoiceForm(forms.Form):
    bill_to = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(initial=datetime.date.today)

class ItemForm(forms.Form):
    item_name = forms.CharField()
    item_count = forms.DecimalField()
    item_price = forms.DecimalField()

ItemFormSet = formset_factory(ItemForm)
