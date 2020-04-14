from django.shortcuts import render, redirect
# from django.http import JsonResponse
from .models import Product
from .forms import ProductForm, RawProductForm

def product_list_view(request):
    products = Product.objects.all()
    context = {
            "products": products
    }
    return render(request, 'products/product_list.html', context)
    # return JsonResponse(list(products.values()), safe=False)


def product_edit_view(request, id):
    product = Product.objects.get(id=id)

    if request.POST and "action" in request.POST and request.POST['action'] == "DELETE":
        product.delete()
        return redirect('/products/')

    form = ProductForm(request.POST or None, instance=product)

    if request.POST and form.is_valid():
        form.save()

    context = {'form': form}
    return render(request, 'products/product_create.html', context)


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    context = {
            'product': product
    }
    return render(request, 'products/product_detail.html', context)



def product_create_view(request):
   form = ProductForm(request.POST or None)
   if form.is_valid():
       form.save()
       form = ProductForm()
   context = {
           'form': form
   }
   return render(request, 'products/product_create.html', context)

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#             'form': my_form
#     }
#     return render(request, 'products/product_create.html', context)



