// Call the dataTables jQuery plugin
$(document).ready(function () {
    $('#dataTable').DataTable({
        language: {
            "lengthMenu": "Mostrar _MENU_ resultados",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ resultados",
            "search": "Pesquisar:",
            "paginate": {
                "previous": "Anterior",
                "next": "Próximo"
            }
        }
    });
});
