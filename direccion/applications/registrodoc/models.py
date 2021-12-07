from django.db import models

# Create your models here.

class Administracion(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)
    """Model definition for MODELNAME."""

    
    class Meta:        

        verbose_name = 'secretaria'
        verbose_name_plural = 'Secretaria de la institucion'
        ordering = ['name']

    def __str__(self):
       
        return self.name

class Materia(models.Model):

    name = models.CharField('Nombre', max_length=50)
    
    
    class Meta:
        """Meta definition for Materia."""

        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['name']

        

    def __str__(self):
        """Unicode representation of Materia."""
        return self.name
    
   
class Docente(models.Model):
       
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=150, blank= True)
    age = models.IntegerField('Edad')    
    
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    avatar = models.ImageField("Imagen", upload_to='registrodoc', height_field=None, width_field=None, max_length=None, blank = True)

       

    class Meta:
        """Meta definition for Docente."""

        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        """Unicode representation of Docente."""
        return self.last_name + ", " + self.first_name
        

class NoDocente(models.Model):
       
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=150, blank= True)
    age = models.IntegerField('Edad')    
       
    administracion = models.ForeignKey(Administracion, on_delete = models.CASCADE)
    avatar = models.ImageField("Imagen", upload_to='registrodoc', height_field=None, width_field=None, max_length=None, blank = True)
       

    class Meta:
        """Meta definition for NoDocente."""

        verbose_name = 'NoDocente'
        verbose_name_plural = 'NoDocentes'

    def __str__(self):
        """Unicode representation of NoDocente."""
        return self.last_name + ", " + self.first_name
        
                