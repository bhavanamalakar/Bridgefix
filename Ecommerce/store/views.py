from .models import Product,Order,OrderItem,Cart
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from accounts.decorators import role_required
from django.core.exceptions import PermissionDenied

@login_required
def product_list(request):
    user_roles = list(request.user.role.values_list('name', flat=True))
    is_seller = 'Seller' in user_roles
    is_customer = 'Customer' in user_roles
    is_admin  = 'Admin' in user_roles

    products = Product.objects.all()

    return render(request, 'product_list.html', {
        'products': products,
        'user_roles': user_roles,
        'is_seller': is_seller,
        'is_customer': is_customer,
        'is_admin' : is_admin,
        'user': request.user,
    })

@role_required(['Seller','Admin'])
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

@role_required(['Seller','Admin'])
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    r=[role.name for role in request.user.role.all()]

    if request.user != product.seller and 'Admin' not in r:        
        raise PermissionDenied("You do not have permission to edit")
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})

@role_required(['Seller','Admin'])
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    r=[role.name for role in request.user.role.all()]

    if request.user != product.seller and 'Admin' not in r:        
        raise PermissionDenied("You do not have permission to delete")
    product.delete()
    return redirect('product_list')


@role_required(['Customer'])
def add_cart(request,pk):
    product=Product.objects.get(id=pk)
    cart,created=Cart.objects.get_or_create(user=request.user,product=product)
    if not created:
        cart.quantity += 1
    cart.save()
    return redirect('cart')

def increase_quantity(request,pk):
    cart_item=get_object_or_404(Cart,pk=pk)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('cart')

def decrease_quantity(request,pk):
    cart_item=get_object_or_404(Cart,pk=pk)
    if cart_item.quantity>1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items=Cart.objects.filter(user=request.user).select_related('product')
    total_price=sum(item.product.price * item.quantity for item in cart_items)
    return render(request,'cart.html',{'cart_items':cart_items,'total_price':total_price})

def remove_from_cart(request, item_id):
    cart_item = Cart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')

@role_required(['Customer'])
def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method=='POST':
        quantity = int(request.POST.get('quantity', 1))
        price=product.price*quantity
        order=Order.objects.create(user=request.user, total_price=price)
        OrderItem.objects.create(order=order, product=product,quantity=quantity,price=product.price)

        return redirect('order_success') 
    return redirect('product_list')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    return render(request, 'my_orders.html', {'orders': orders})

@login_required
def order_success(request):
    return render(request, 'order_success.html')
