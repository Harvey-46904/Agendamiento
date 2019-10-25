from django.db import models

# Create your models here.
class Genero(models.Model):
    id= models.AutoField(primary_key=True)
    title=models.CharField('Nombre',max_length=150)
    class Meta:
        verbose_name='Gender'
        verbose_name_plural='Genders'
    def __str__(self):
        return self.title

class paciente(models.Model):
    id_paciente=models.CharField('Cedula',max_length=50,primary_key=True)
    Primer_Nombre=models.CharField('Primer Nombre',max_length=30)
    Segundo_Nombre=models.CharField('Segundo Nombre',max_length=30)
    Primer_Apellido=models.CharField('Primer Apellido',max_length=30)
    Segundo_Apellido=models.CharField('Segundo Apellido',max_length=30)
    Nacimiento = models.DateField('Fecha Nacimiento')
    Genero=models.ForeignKey(Genero,on_delete=models.CASCADE)
    Telefono=models.BigIntegerField('Telefono')
    class Meta:
        verbose_name='Paciente'
        verbose_name_plural='Pacientes'
    def __str__(self):
        letra='{0} {1}'.format(self.Primer_Nombre,self.Primer_Apellido)
        return  letra