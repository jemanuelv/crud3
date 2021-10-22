from django.shortcuts import render, redirect
from .models import Employee, Presupuesto, Placas
from .forms import EmployeesForm, PresupuestoFormNew, PresupuestoFormEdit, PlacasForm



def start (request):
    return render(request, 'app/start.html')
    
  

# ---- List ----

  
def employees_list (request):
    
    Table = Employee.objects.all()  
    return render(request, 'app/employees_list.html', {'Table':Table})
    
def presupuesto_list (request):
    
    Table = Presupuesto.objects.all()  
    return render(request, 'app/presupuesto_list.html', {'Table':Table})  

def placas_list (request):
    
    Table = Placas.objects.all()  
    return render(request, 'app/placas_list.html', {'Table':Table}) 

# ---- New ----

def employees_new(request):  
    if request.method == "POST":  
        form = EmployeesForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/app/employees_list')  
            except:  
                pass  
    else:  
        form = EmployeesForm()  
    
    return render(request,'app/employees_new.html',{'form':form})


def presupuesto_new(request):  
    if request.method == "POST":  
        form = PresupuestoFormNew(request.POST)  

        
        if form.is_valid():  
            
        
            try:  
                
       
                PresupuestoObject=form.save()  
                eid='PRES-DEEI-MAIT-'+form.data['egerencia']+'-'+form.data['ept']+'-'+form.data['ewp']+'-'+form.data['enumber']+'-'+form.data['eversion']
                
                PresupuestoObject.eid=eid
                PresupuestoObject.save()
     
                
                
                return redirect('/app/presupuesto_list')  
            except:  
           
                pass  
    else:  
        form = PresupuestoFormNew()  
    
    return render(request,'app/presupuesto_new.html',{'form':form})



def placas_new(request):  
    if request.method == "POST":  
        form = PlacasForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/app/placas_list')  
            except:  
                pass  
    else:  
        form = PlacasForm()  
    
    return render(request,'app/placas_new.html',{'form':form})

# ---- Edit ----

def employees_edit(request, id):  
    
    row = Employee.objects.get(id=id)
    
    
    if request.method == "POST":  
        form = EmployeesForm(request.POST, instance = row)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/app/employees_list')  
            except:  
                pass  
    else:  
        form = EmployeesForm(instance = row) 
    
    return render(request,'app/employees_edit.html',{'form':form, 'row':row})
    
    
def presupuesto_edit(request, id):  
    
    row = Presupuesto.objects.get(id=id)
    
    if request.method == "POST":  
        form = PresupuestoFormEdit(request.POST, instance = row)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/app/presupuesto_list')  
            except:  
                pass  
    else:  
        form = PresupuestoFormEdit(instance = row) 
    
    return render(request,'app/presupuesto_edit.html',{'form':form, 'row':row})
    
def placas_edit(request, id):  
    
    row = Placas.objects.get(id=id)
    
    if request.method == "POST":  
        form = PlacasForm(request.POST, instance = row)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/app/placas_list')  
            except:  
                pass  
    else:  
        form = PlacasForm(instance = row) 
    
    return render(request,'app/placas_edit.html',{'form':form, 'row':row}) 

# ---- Copy ----

def placas_copy(request, id):  
    
    row = Placas.objects.get(id=id)
    row.pk = None
    row.save()
    
    return redirect('/app/placas_list')  



# ---- Destroy ----


def employees_destroy(request, id):  
    row = Employee.objects.get(id=id)  
    row.delete()  
    return redirect('/app/employees_list')
    
def presupuesto_destroy(request, id):  
    row = Presupuesto.objects.get(id=id)  
    row.delete()  
    return redirect('/app/presupuesto_list')
    
def placas_destroy(request, id):  
    row = Placas.objects.get(id=id)  
    row.delete()  
    return redirect('/app/placas_list')