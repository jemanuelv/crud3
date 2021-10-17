from django import forms
from .models import Employee, Presupuesto, Placas

class EmployeesForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  
        

class PresupuestoFormEdit(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['efecha', 'edescripcion', 'eautor']

        widgets = {
            'efecha': forms.TextInput(attrs={'readonly':'readonly'}),
        }

class PresupuestoFormNew(PresupuestoFormEdit):
    
    pt_choices= [
    ('0333', '0333'),
    ('0804', '0804'),
    ('0874', '0874'),]
    
    ept = forms.CharField(label='PT', max_length=4, widget=forms.Select(choices=pt_choices))
    ewp = forms.CharField(label='WP', max_length=6, widget=forms.TextInput(attrs={'size': '6'}))
    enumber = forms.CharField(label='Number', max_length=3, widget=forms.TextInput(attrs={'size': '3'}))
    eversion = forms.CharField(label='Version', max_length=1, widget=forms.TextInput(attrs={'size': '1'}))
 
class PlacasForm(forms.ModelForm):  
    class Meta:  
        model = Placas
        fields = "__all__" 