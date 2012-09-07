# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from invoice.models import Invoice, InvoiceItem, Item
from invoice.forms import InvoiceForm, ItemFormSet

def generate(request, invoice_id, key):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if invoice.secret_key == key:
        return render(request, 'invoice/invoice.html', {'invoice': invoice})
    else:
        raise HttpResponseForbidden

@login_required
def index(request):
    invoices = Invoice.objects.filter(user=request.user)
    return render(request, 'invoice/index.html', {'invoices': invoices})

@login_required
def create(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        item_formset = ItemFormSet(request.POST) 
        if invoice_form.is_valid() and item_formset.is_valid():
            invoice_form.clean()
            item_formset.clean()
            new_invoice = Invoice(bill_to=invoice_form['bill_to'].data,
                    date=invoice_form['date'].data, user=request.user)
            new_invoice.save()
            for form in item_formset:
                print form.cleaned_data
                print form['item_price'].data
                new_item = Item(name=form['item_name'].data,
                    price=form['item_price'].data, user=request.user)
                new_item.save()
                print type(new_item.price)
                new_invoice_item = InvoiceItem(count=form['item_count'].data,
                        item=new_item, user=request.user)
                new_invoice_item.save()
                new_invoice.items.add(new_invoice_item)
            new_invoice.save()
            return redirect('/dashboard/') 
    else:
        invoice_form = InvoiceForm()
        item_formset = ItemFormSet()
    return render(request, 'invoice/create.html', {'invoice_form': invoice_form,
                                'item_formset': item_formset,
                                'form_counter': len(item_formset.forms) - 1,})
