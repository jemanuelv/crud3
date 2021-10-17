src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.min.js">

$(document).ready(function() {
	
	$('#table_list').DataTable({
		stateSave: true,
			"language": {
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "No se encontraron resultados",
            "info": "Página _PAGE_ de _PAGES_",
            "infoEmpty": "No hay registros disponibles",
            "infoFiltered": "(filtrado desde _MAX_ registros totales)",
			"search": "Buscar:",
			"paginate": {
				"first":      "Primero",
				"last":       "Ultimo",
				"next":       "Siguiente",
				"previous":   "Anterior"
			},
	    }
	});
}) 
	

function showdelete(id)
{
	$('#autoid').val(id);  
	$('#myModal').modal('show');
}


function deleteid()
{
	var delete_id= $('#autoid').val();
    var table_name= $('#table_name').val();
	url='/app/'+table_name+'_delete/'+delete_id;
    
	$('#myModal').modal('hide');
	
	window.location.href = url

           
}

