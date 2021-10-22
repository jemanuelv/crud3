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

        widgets = {'efecha': forms.SelectDateWidget()
        }


class PresupuestoFormNew(PresupuestoFormEdit):
    
    pt_choices= [
    ('0333', '0333'),
    ('0804', '0804'),
    ('0874', '0874'),]
    
    gerencia_choices= [
    ('GNE', 'GNE'),
    ('GNG', 'GNG'),
    ('GNU', 'GNU'),]
    
    egerencia = forms.CharField(label='Gerencia', max_length=3, widget=forms.Select(choices=gerencia_choices))
    ept = forms.CharField(label='PT', max_length=4, widget=forms.Select(choices=pt_choices))
    ewp = forms.CharField(label='WP', max_length=6, widget=forms.TextInput(attrs={'size': '6'}))
    enumber = forms.CharField(label='Number', max_length=3, widget=forms.TextInput(attrs={'size': '3'}))
    eversion = forms.CharField(label='Version', max_length=1, widget=forms.TextInput(attrs={'size': '1'}))
 
class PlacasForm(forms.ModelForm):  
    
    epresupuesto = forms.ModelChoiceField(queryset=Presupuesto.objects.all().order_by('eid'), 
                            empty_label="Seleccione un presupuesto", 
                            widget=forms.Select(attrs={'class': 'form-control', 'style':'width:auto'}))
  
    class Meta:  
        model = Placas
        fields = "__all__" 
        widgets = {         
            'etipo': forms.Select (attrs={'class': 'form-control', 'style':'width:auto'}),
            'edescripcion': forms.Textarea (attrs={'class': 'form-control', 'cols':'40', 'rows':'4'}),
            'qplacas': forms.NumberInput (attrs={'class': 'form-control',  'style':'width: 7em'}),
            'qcomponentes': forms.NumberInput (attrs={'class': 'form-control', 'style':'width: 7em'}),
            'qBOM': forms.NumberInput (attrs={'class': 'form-control', 'style':'width: 7em'}),
            'efaz': forms.RadioSelect(attrs={'class':'form-check-input'}),
            'qpads': forms.NumberInput (attrs={'class': 'form-control', 'style':'width: 3em', 'min':'0', 'max':'100'}),
            'qaut': forms.NumberInput (attrs={'class': 'form-control', 'style':'width: 3em', 'min':'0', 'max':'100'}),
            'qfine_pitch': forms.NumberInput (attrs={'class': 'form-control', 'style':'width: 7em'}),
            'qBGA_CCGA': forms.NumberInput (attrs={'class': 'form-control', 'style':'width: 7em'}),
            'epolimeros': forms.CheckboxInput (attrs={'class':'form-check-input'}),
            'ePEM': forms.CheckboxInput (attrs={'class':'form-check-input'}),
            'ecompras': forms.TextInput (attrs={'class': 'form-control', 'style':'width: 4em'}),
            'ecalidad':  forms.Select (attrs={'class': 'form-control', 'style':'width:auto'}),
            'emaduro': forms.CheckboxInput (attrs={'class':'form-check-input'}),
            'elote': forms.CheckboxInput (attrs={'class':'form-check-input'}),
            'PE': forms.NumberInput (attrs={'class': 'form-control',  'style':'width: 7em', 'min':'0'}),
            'QA': forms.NumberInput (attrs={'class': 'form-control',  'style':'width: 7em', 'min':'0'}),
            'QC': forms.NumberInput (attrs={'class': 'form-control',  'style':'width: 7em', 'min':'0'}),
            
        }
        
