from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()

    def __str__(self):
        return self.name    

class Inventory(models.Model):
    name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    unit_price=models.IntegerField()
    

    def __str__(self):
        return self.name    

class Order(models.Model):
    name=models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    table_name=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return str(self.name)

    def update_ingredients_quantity(self):
        recipe = self.name.recipe.all()
        for ingredient in recipe:
            ingredient_instance = Inventory.objects.get(name=ingredient.ingredient.name)
            ingredient_instance.quantity -= ingredient.quantity * self.quantity
            ingredient_instance.save()



class Recipe(models.Model):
     name = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='recipe')
     ingredient = models.ForeignKey(Inventory, on_delete=models.CASCADE)
     quantity = models.FloatField()    

def __str__(self):
        return f"{self.name} - {self.quantity}"


