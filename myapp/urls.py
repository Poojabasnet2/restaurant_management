
from django.urls import path
from django.views import *
from .views import *
from .import views
app_name="myapp"
urlpatterns = [
    path('', views.HomePage.as_view(), name='base'),  # Homepage
    path('menu/', views.MenuList.as_view(), name='menu'),  # Menu list
    path('add/menu/', views.AddItem.as_view(), name='add_item'),  # Add menu item
    path('inventory/', views.InventoryList.as_view(), name='inventory'),  # Inventory
    path('add/inventory/', views.AddInventory.as_view(), name='add_inventory'),
    path('<pk>/update/',views.InventoryUpdateView.as_view(), name='inventoryupdate'),
    path('<pk>/delete/',views.InventoryDelete.as_view(), name='delete'),
    path('order/', views.OrderList.as_view(), name='order'),
    path('add/order/', views.AddOrder.as_view(), name='add_order'),
    # path('<pk>/delete/', views.DeleteOrder.as_view(), name='delete_order'),

    path('recipe/', views.RecipeList.as_view(), name='recipe'),
    path('add/recipe/', views.AddRecipe.as_view(), name='add_recipe'),
]

