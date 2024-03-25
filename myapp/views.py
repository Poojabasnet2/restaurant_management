from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Menu,Inventory,Order,Recipe
from django.urls import reverse_lazy
from myapp.forms import MenuForm
from myapp.forms import InventoryForm,OrderForm,RecipeForm
from django.views import View
# Create your views here.

class HomePage(View):
    def get(self, request):
        return render(request, 'myapp/base.html')

class MenuList(ListView):
    
    model=Menu
    context_object_name='list'
    template_name="myapp/menu.html"

class AddItem(CreateView):
    
    model=Menu
    form_class=MenuForm
    template_name='myapp/add_item.html'
    success_url=reverse_lazy('myapp:menu')


class InventoryList(ListView):
    model=Inventory
    context_object_name='inventory'
    template_name="myapp/inventory.html"

class AddInventory(CreateView):
    
    model=Inventory
    form_class=InventoryForm
    template_name='myapp/add_inventory.html'
    success_url=reverse_lazy('myapp:inventory')

class InventoryUpdateView(UpdateView):
    model=Inventory
    form_class=InventoryForm
    template_name="myapp/add_inventory.html"
    success_url=reverse_lazy('myapp:inventory') 
class InventoryDelete(DeleteView):
    model=Inventory
    success_url=reverse_lazy('myapp:inventory')

class OrderList(ListView):
    model=Order
    context_object_name='order'
    template_name="myapp/order.html"


class AddOrder(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "myapp/add_order.html"
    success_url = reverse_lazy('myapp:order')

    
    
# class DeleteOrder(DeleteView):
#     model = Order
#     success_url = reverse_lazy('myapp:order')


class RecipeList(ListView):
    model=Recipe
    context_object_name='recipe'
    template_name="myapp/recipe.html"

class AddRecipe(CreateView):
    
    model=Recipe
    form_class=RecipeForm
    template_name="myapp/add_recipe.html"
    success_url=reverse_lazy('myapp:recipe')

    