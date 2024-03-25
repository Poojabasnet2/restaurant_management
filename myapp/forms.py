from django import forms
from myapp.models import Menu,Inventory,Order,Recipe

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(),
            'price': forms.TextInput(),
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'quantity','unit_price']
        widgets = {
            'name': forms.TextInput(),
            'quantity': forms.TextInput(),
            'unit_price': forms.TextInput(),
        }

from django import forms
from myapp.models import Menu,Inventory,Order,Recipe

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(),
            'price': forms.TextInput(),
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'quantity','unit_price']
        widgets = {
            'name': forms.TextInput(),
            'quantity': forms.TextInput(),
            'unit_price': forms.TextInput(),
        }

class OrderForm(forms.ModelForm):
    def __init__(self,  **kwargs):
        super(OrderForm, self).__init__( **kwargs)
        # Set initial value for order_item
        default_name = Menu.objects.first()  # Get the first menu item
        if default_name:
            self.fields['name'].initial = default_name
            

    class Meta:
        model = Order
        fields = ['name', 'quantity','table_name']
        widgets = {
            'quantity': forms.TextInput(),
            
        }

class RecipeForm(forms.ModelForm):
    def __init__(self,  **kwargs):
        super(RecipeForm, self).__init__( **kwargs)
        # Set initial value for order_item
        default_name = Menu.objects.first()  # Get the first menu item
        if default_name:
            self.fields['name'].initial = default_name
            

    class Meta:
        model = Recipe
        fields = ['name', 'ingredient','quantity']
        widgets = {
            'quantity': forms.TextInput(),
            
        }




class OrderForm(forms.ModelForm):
    def __init__(self,  **kwargs):
        super(OrderForm, self).__init__(**kwargs)
        # Set initial value for order_item
        default_menu_item = Menu.objects.first()  # Get the first menu item
        if default_menu_item:
            self.fields['name'].initial = default_menu_item

    class Meta:
        model = Order
        fields = ['name', 'quantity', 'table_name']
        widgets = {
            'quantity': forms.TextInput(),
            'table_name': forms.TextInput(),
        }


    name= forms.ModelChoiceField(queryset=Menu.objects.all(), widget=forms.Select)

    def save(self, commit=True):
        order = super(OrderForm, self).save(commit=False)
        if commit:
            order.save()  # Save the order first
            order.update_ingredients_quantity()  # Update ingredient quantities
        return order

class RecipeForm(forms.ModelForm):
    def __init__(self,  **kwargs):
        super(RecipeForm, self).__init__( **kwargs)
        # Set initial value for order_item
        default_name = Menu.objects.first()  # Get the first menu item
        if default_name:
            self.fields['name'].initial = default_name
            

    class Meta:
        model = Recipe
        fields = ['name', 'ingredient','quantity']
        widgets = {
            'quantity': forms.TextInput(),
            
        }




