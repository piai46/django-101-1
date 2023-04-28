from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.


def product_list_view(request):
    queryset = Product.objects.all()
    context = {'object_list': queryset}
    return render(request, 'products/product_list.html', context)


def product_detail_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


# Raw Product Form
def product_create_view2(request):
    form = RawProductForm()
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
    context = {'form': form}
    return render(request, 'products/product_create.html', context=context)


# Product form
@login_required
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/products/')
    context = {'form': form}
    return render(request, 'products/product_create.html', context=context)


@login_required
def product_edit_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, 'products/product_edit.html', context)


@login_required
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {'object': obj}
    return render(request, 'products/product_delete.html', context=context)
