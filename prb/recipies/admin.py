from django.contrib import admin
import nested_admin
from recipies.models import recipie, item, itemlist, shoppingitem

# Register your models here.

class ShoppingitemInline(nested_admin.NestedStackedInline):
    model = shoppingitem.Shoppingitem

class ItemInline(nested_admin.NestedStackedInline):
    model = item.Item

class ItemlistInline(nested_admin.NestedStackedInline):
    model = itemlist.Itemlist
    inlines = [
            ItemInline,
            ]

class RecipieAdmin(nested_admin.NestedModelAdmin):
    inlines = [
            ItemlistInline,
            ShoppingitemInline,
            ]

admin.site.register(recipie.Recipie, RecipieAdmin)
