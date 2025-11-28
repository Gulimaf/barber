from django.db import models

# Create your models here.
class Agendamentos(models.Model):
    telefone_cliente = models.CharField(max_length=20)
    data = models.DateTimeField()
    servico = models.CharField(max_length=100)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'agendamentos'