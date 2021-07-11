from django.contrib import admin
from .models import Cliente, Cuenta, Deposito, Retiro

#-------------------------------------------------------------------------
admin.site.register(Cliente)
#--------------------------------------------------------------------------
#class CuentaAdmin(admin.ModelAdmin):
#    list_display = ('id', 'fecha_registro', 'estado', 'saldo', 'cliente')
#    list_editable = ('cliente',)

admin.site.register(Cuenta),#CuentaAdmin)
# ------------------------------------------------------------------------
admin.site.register(Deposito)
# ------------------------------------------------------------------------
admin.site.register(Retiro)