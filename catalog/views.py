from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product, Order


def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'orders/product.html', context)


def order_add(request, product_id):
    product = Product.objects.get(id=product_id)
    order = Order.objects.filter(user=request.user, product=product)

    if not order.exists():
        Order.objects.create(user=request.user, product=product, quantity=1)
    else:
        order = order.first()
        order.quantity += 1
        order.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
