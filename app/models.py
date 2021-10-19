from django.db import models
from datetime import date

class Employee(models.Model):  

    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
    def __str__(self):
        return "%s" % (self.ename)
    
    class Meta:  
        db_table = "employee"
        
        
class Presupuesto(models.Model):
    eid = models.CharField(max_length=20) 
    efecha = models.DateField(default=date.today)
    edescripcion = models.TextField(max_length=256)
    eautor = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s" % (self.eid)
    
    
    class Meta:
        db_table = "presupuesto"
        
        
class Placas(models.Model):
    epresupuesto = models.ForeignKey(Presupuesto, on_delete=models.CASCADE)
    
    tipo_choices= [
    ('EL-1655', 'EL-1655'),
    ('EL-1656', 'EL-1656'),
    ('EL-1666', 'EL-1666'),]
        
    
    
    etipo = models.CharField(max_length=8, choices=tipo_choices)
    
    
    edescripcion = models.TextField(max_length=256)

    class Meta:
        db_table = "placas"
