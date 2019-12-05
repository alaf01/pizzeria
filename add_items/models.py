from django.db import models

class Ingredient(models.Model):
    ingredient=models.CharField(max_length=64,null=True, blank=True)
    price=models.FloatField(null=True, blank=True, default=3)

    def __str__(self):
        return f"{self.ingredient}"
class Dough_flour(models.Model):
    flour=models.CharField(max_length=16)
    add_fee=models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.flour} flour"

class Dough_size(models.Model):
    size=models.CharField(max_length=16)
    price=models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.size}"

class Dough_thickness(models.Model):
    thickness=models.CharField(max_length=16)
    add_fee=models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.thickness}"
    class Meta:
        verbose_name_plural = "Dough_thickness"


class Sauce(models.Model):
    sauce=models.CharField(max_length=32, null=True, blank=True)
    add_fee=models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.sauce}"

class Pizza_menu(models.Model):
    name = models.CharField(max_length=30,null=True, blank=True,)
    sauce = models.ForeignKey(Sauce, null=True, blank=True, on_delete=models.CASCADE, related_name="menu_sauce")
    ingredient = models.ManyToManyField(Ingredient, related_name="menu_ingredients")
    price=models.FloatField(null=True, blank=True, default=10)
    def __str__(self):
        return f"{self.name}"

class Pizza_compose(models.Model):
    pizza_size = models.ForeignKey(Dough_size, default="small", on_delete=models.CASCADE, related_name="pizza_size")
    flour = models.ForeignKey(Dough_flour, default="white", on_delete=models.CASCADE, related_name="pizza_flour")
    thickness = models.ForeignKey(Dough_thickness, default="thin", on_delete=models.CASCADE, related_name="pizza_thickness")
    sauce = models.ForeignKey(Sauce, null=True, blank=True, on_delete=models.CASCADE, related_name="compose_sauce")
    ingredient = models.ManyToManyField(Ingredient, related_name="compose_ingredients")

    def __str__(self):
        return f"{self.name}"
