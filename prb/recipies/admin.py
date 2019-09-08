from django.contrib import admin
import nested_admin
from recipies.models import recipie, item, itemlist, shoppingitem

# Register your models here.

class ShoppingitemInline(nested_admin.NestedTabularInline):
    model = shoppingitem.Shoppingitem
    extra = 0

class ItemInline(nested_admin.NestedTabularInline):
    model = item.Item
    extra = 0

class ItemlistInline(nested_admin.NestedStackedInline):
    model = itemlist.Itemlist
    extra = 0
    inlines = [
            ItemInline,
            ]

class RecipieAdmin(nested_admin.NestedModelAdmin):
    inlines = [
            ItemlistInline,
            ShoppingitemInline,
            ]

admin.site.register(recipie.Recipie, RecipieAdmin)
