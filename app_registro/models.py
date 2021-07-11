from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    fechanacimiento = models.DateField()
    telefono = models.CharField(max_length=25)
    correo = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Cuenta(models.Model):
    ESTADOS = (
        ('1', 'Activo'),
        ('2', 'Inactivo'),
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)
    #estado = models.BooleanField(default=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='1')
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    @property
    def saldo_actual(self):
        cant_deposito = self.cantidad_set.count()
        return self.saldo - cant_deposito

    def __str__(self):
        return f'{self.cliente}'


class Deposito(models.Model):
    fecha_deposito = models.DateTimeField(auto_now_add=True)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.fecha_deposito}'

class Retiro(models.Model):
    fecha_retiro = models.DateTimeField(auto_now_add=True)
    Cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.fecha_retiro}'