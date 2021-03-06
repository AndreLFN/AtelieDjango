from django.contrib import admin

from .models import Registro, Produto, Venda, ItemVenda
# Register your models here.

admin.site.register(Registro)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ItemVenda)