from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product, Sale
from .forms import SaleForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'pos/product_list.html', {'products': products})

def add_sale(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.product = product
            sale.save()
            # Generate the URL pattern for the 'receipt' view using reverse
            return redirect(reverse('pos_app:receipt', kwargs={'sale_id': sale.id}))
    else:
        form = SaleForm()

    return render(request, 'pos/add_sale.html', {'form': form, 'product': product})

def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'pos/sales_list.html', {'sales': sales})

# def receipt(request, sale_id):
#     sale = get_object_or_404(Sale, id=sale_id)
#     return render(request, 'pos/receipt.html', {'sale': sale})
def receipt(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    total_price = (sale.quantity or 0) * sale.product.price
    context = {
        'sale': sale,
        'total_price': total_price,
    }
    return render(request, 'pos/receipt.html', context)
