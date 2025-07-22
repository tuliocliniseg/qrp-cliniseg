from django.contrib import admin
from .models import Empresa, Setor

class SetorInline(admin.TabularInline):
    model = Setor
    extra = 1

class EmpresaAdmin(admin.ModelAdmin):
    inlines = [SetorInline]

admin.site.register(Empresa, EmpresaAdmin)
