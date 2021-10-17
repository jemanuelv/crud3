from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.start, name='start'),
    path('employees_list', views.employees_list, name='employees_list'),
    path('employees_new', views.employees_new, name='employees_new'),
    path('employees_delete/<int:id>', views.employees_destroy),
    path('employees_edit/<int:id>', views.employees_edit),
    path('presupuesto_list', views.presupuesto_list, name='presupuesto_list'),
    path('presupuesto_new', views.presupuesto_new, name='presupuesto_new'),
    path('presupuesto_delete/<int:id>', views.presupuesto_destroy),
    path('presupuesto_edit/<int:id>', views.presupuesto_edit),
    path('placas_list', views.placas_list, name='EL-1655_list'),
    path('placas_new', views.placas_new, name='EL-1655_new'),
    path('placas_delete/<int:id>', views.placas_destroy),
    path('placas_edit/<int:id>', views.placas_edit),
   
]
 
