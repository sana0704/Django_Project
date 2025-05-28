from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

from .models import Product
def homeView(request):
    prods=Product.objects.all()
    context={ 
        'products': prods
    }
    template ='home.html'
    return render(request,template,context) #this renders the response acc to the request using the context

# read
class ProductDetails(DetailView):
    model = Product
    template_name='product_details.html'
    context_object_name = 'product'

# insert
class AddProduct (CreateView):
    model = Product
    fields ='__all__'
    template_name = 'add_product.html'
    success_url ='/'


# editproduct

class EditProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name='edit_product.html'
    success_url='/'
# delete

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = '/'