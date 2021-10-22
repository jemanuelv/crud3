from django.db import models
from datetime import date

class Employee(models.Model):  

    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15, blank=True)
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
    (None, ''),
    ('EL-1655', 'EL-1655'),
    ('EL-1656', 'EL-1656'),
    ('EL-1666', 'EL-1666'),]
        
    etipo = models.CharField(max_length=8, choices=tipo_choices)
    
    edescripcion = models.TextField(max_length=256, blank=True)
    
    qplacas = models.PositiveIntegerField() 
    qcomponentes = models.PositiveIntegerField()
    qBOM = models.PositiveIntegerField()
    
    faz_choices= [
    ('SIMPLE', 'SIMPLE'),
    ('DOBLE', 'DOBLE')
    ]
    
    efaz = models.CharField(max_length=6, choices=faz_choices, default='SIMPLE')
    
    qpads = models.PositiveIntegerField()
    
    qaut = models.PositiveIntegerField()
    
    qfine_pitch = models.PositiveIntegerField()
    
    qBGA_CCGA = models.PositiveIntegerField()
    
    epolimeros = models.BooleanField()
    
    ePEM = models.BooleanField()
    
    ecompras= models.CharField(max_length=3)
    
    calidad_choices= [
    (None, ''),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ]
    
    ecalidad = models.CharField(max_length=1, choices=calidad_choices)
    
    emaduro = models.BooleanField()
    
    elote = models.BooleanField()
    
    PE = models.DecimalField(decimal_places=2, max_digits=7,  null=True)
    QA = models.DecimalField(decimal_places=2, max_digits=7,  null=True)
    QC = models.DecimalField(decimal_places=2, max_digits=7,  null=True)
    
  

    class Meta:
        db_table = "placas"
