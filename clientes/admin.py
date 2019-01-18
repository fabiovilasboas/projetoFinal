from django.contrib import admin
from .models import Person, Documento, Vendas, Produto

# Register your models here.
admin.site.register(Person)
admin.site.register(Documento)
admin.site.register(Vendas)
admin.site.register(Produto)