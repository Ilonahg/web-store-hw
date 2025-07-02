from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required
from .models import Product
from .forms import ProductForm  # если используешь форму
from .forms import ProductForm

# Список продуктов
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Детали продукта
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

# Создание продукта (автоматически ставится owner)
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

# Редактирование продукта (только для владельца)
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user != product.owner:
        raise PermissionDenied

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/product_form.html', {'form': form})

# Удаление продукта (владелец или модератор)
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.user == product.owner or request.user.groups.filter(name='Модератор продуктов').exists():
        product.delete()
        return redirect('products:list')
    else:
        raise PermissionDenied

# Отмена публикации (только модератор с правом can_unpublish_product)
@permission_required('products.can_unpublish_product', raise_exception=True)
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.status = 'draft'
    product.save()
    return redirect('products:detail', pk=product.pk)

from django.shortcuts import render
from .services import get_products_by_category

def products_by_category_view(request, category_id):
    products = get_products_by_category(category_id)
    return render(request, 'products_by_category.html', {'products': products})
