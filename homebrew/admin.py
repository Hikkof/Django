from django.contrib import admin
from .models import Homebrew, Item, Weapon, Armor, Career


admin.site.register(Homebrew)
admin.site.register(Item)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Career)
