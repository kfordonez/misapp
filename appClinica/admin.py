from django.contrib import admin
from .models import Paciente, Medico, Vendedor, HistorialMedico, Turno, Pedido, Producto, User

#Register your models here.
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Vendedor)
admin.site.register(HistorialMedico)
admin.site.register(Turno)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(User)