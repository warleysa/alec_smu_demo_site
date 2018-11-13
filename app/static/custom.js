 // /static/custom.js

$(document).ready(function() {
    var alecSessionsTable = $('#profile-classes-table').DataTable( {
        "bSortCellsTop": true,
        "bFilter": true,
        "columns": [
            null,
            null,
            null,
            { "orderable": false,
              "searchable": false }
        ],
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return 'Details for '+data[0]+' '+data[1];
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tutorTable: 'table'
                } )
            }
        },
        initComplete: function () {
            this.api().columns([0, 1, 2]).every( function () {
                var column = this;
                var columnIndex = this.index();
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $("#filter-profile-classes th:eq("+columnIndex+")").empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        }
    } );
});


$(document).ready(function() {
    var alecSessionsTable = $('#alec-sessions-table').DataTable( {
        "bSortCellsTop": true,
        "bFilter": true,
        "columns": [
            null,
            null,
            null,
            { "orderable": false,
              "searchable": false }
        ],
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return 'Details for '+data[0]+' '+data[1];
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tutorTable: 'table'
                } )
            }
        },
        initComplete: function () {
            this.api().columns([0, 1]).every( function () {
                var column = this;
                var columnIndex = this.index();
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $("#filter-alec-sessions th:eq("+columnIndex+")").empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        }
    } );
    $('#collapse-alec-sessions-table').on('shown.bs.collapse', function () {
        alecSessionsTable.responsive.recalc();
    })
});

$(document).ready(function() {
    var classesStatsTable = $('#classes-stats-table').DataTable( {
        "bSortCellsTop": true,
        "bFilter": true,
        "columns": [
            null,
            null,
            null,
            { "orderable": false,
              "searchable": false }
        ],
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return 'Details for '+data[0]+' '+data[1];
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tutorTable: 'table'
                } )
            }
        },
        initComplete: function () {
            this.api().columns([0, 1]).every( function () {
                var column = this;
                var columnIndex = this.index();
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $("#filter-classes-stats th:eq("+columnIndex+")").empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        }
    } );
    $('#collapse-classes-stats-table').on('shown.bs.collapse', function () {
        classesStatsTable.responsive.recalc();
    })
});

$(document).ready(function() {
    var tutoringSessionsTable = $('#tutoring-sessions-table').DataTable( {
        "bSortCellsTop": true,
        "bFilter": true,
        "columns": [
            null,
            null,
            null,

            { "orderable": false,
              "searchable": false },

            { "orderable": false,
              "searchable": false }
        ],
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return 'Details for '+data[0]+' '+data[1];
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tutorTable: 'table'
                } )
            }
        },
        initComplete: function () {
            this.api().columns([0]).every( function () {
                var column = this;
                var columnIndex = this.index();
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $("#filter-tutor-sessions th:eq("+columnIndex+")").empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        }
    } );
    $('#collapse-tutoring-sessions-table').on('shown.bs.collapse', function () {
        tutoringSessionsTable.responsive.recalc();
    })
});


$(document).ready(function() {
    var tutorTable = $('#tutors-table').DataTable( {
        "bSortCellsTop": true,
        "bFilter": true,
        "columns": [
            null,
            { "orderable": false,
              "searchable": false },

            { "orderable": false,
              "searchable": false },

            { "orderable": false,
              "searchable": false },

            { "orderable": false,
              "searchable": false }
        ],
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return 'Details for '+data[0]+' '+data[1];
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tutorTable: 'table'
                } )
            }
        },
        initComplete: function () {
            this.api().columns([0, 1, 2]).every( function () {
                var column = this;
                var columnIndex = this.index();
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $("#filter-tutors th:eq("+columnIndex+")").empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        }
    } );
    $('#collapse-tutor-table').on('shown.bs.collapse', function () {
        tutorTable.responsive.recalc();
    })
});

$(document).ready(function() {
    var locationTable = $('#location-table').DataTable( {
        "bSortCellsTop": true,
        "bFilter": true,
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return 'Details for '+data[0]+' '+data[1];
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    locationTable: 'table'
                } )
            }
        },
        initComplete: function () {
            this.api().columns([0, 1, 2]).every( function () {
                var column = this;
                var columnIndex = this.index();
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $("#filter-location th:eq("+columnIndex+")").empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        }
    } );
});

$(document).ready(function() {
    var classTable = $('#classes-table').DataTable( {
        "bSortCellsTop": true,
        "bFilter": true,
        "columns": [
            null,
            null,
            null,
            { "orderable": false },

            { "orderable": false,
              "searchable": false },

            { "orderable": false,
              "searchable": false }
        ],
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return 'Details for '+data[0]+' '+data[1];
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tableClass: 'table'
                } )
            }
        },
        initComplete: function () {
            this.api().columns([0, 1, 2]).every( function () {
                var column = this;
                var columnIndex = this.index();
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $("#filter-classes th:eq("+columnIndex+")").empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );
 
                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );
 
                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        }
    } );
    $('#collapse-class-table').on('shown.bs.collapse', function () {
        classTable.responsive.recalc();
    })
});


// $.datetimepicker.setDateFormatter({
//     parseDate: function (date, format) {
//         var d = moment(date, format);
//         return d.isValid() ? d.toDate() : false;
//     },
//     formatDate: function (date, format) {
//         return moment(date).format(format);
//     },
// });

// $('.datetime').datetimepicker({
//     format:'DD-MM-YYYY hh:mm A',
//     formatTime:'hh:mm A',
//     formatDate:'DD-MM-YYYY',
//     useCurrent: false,
// });

// Initialize Pusher
const pusher = new Pusher('989251a250c4490baf73', {
    cluster: 'us2',
    encrypted: true
});

// Subscribe to table channel
var channel = pusher.subscribe('table');

channel.bind('new-class', (data) => {
   $('#classes-table').append(`
        <tr id="${data.data.id}">
            <th scope="row"> ${data.data.dept} </th>
            <td> ${data.data.number} </td>
            <td> ${data.data.class_name} </td>
            <td> ${data.data.desc} </td>
            <td> <a class="btn btn-primary" role="button" href="/edit/${data.data.id}">Edit</a> </td>
            <td> <button class="btn btn-danger" data-toggle="modal" data-target="#confirmation-modal" data-id="${data.data.id}" data-dept="${data.data.dept}" data-number="${data.data.number}">Remove Class</button> </td>
        </tr>
   `)
});

$("#form-class-add").ajaxForm({
    success: function() {
        successMessage('Successfully Added Class...');
        $("#form-class-add").trigger("reset");
    },
    error: function(error) {
        errorMessage('Failed Adding Class...');
    }
});

channel.bind('update-class', (data) => {

    $(`#${data.data.id}`).empty()

    $(`#${data.data.id}`).html(`
        <th scope="row"> ${data.data.dept} </th>
        <td> ${data.data.number} </td>
        <td> ${data.data.class_name} </td>
        <td> ${data.data.desc} </td>
        <td> <a class="btn btn-primary" role="button" href="/edit-class/${data.data.id}">Edit</a> </td>
        <td> <button class="btn btn-danger" data-toggle="modal" data-target="#confirmation-modal" data-id="${data.data.id}" data-dept="${data.data.dept}" data-number="${data.data.number}">Remove Class</button> </td>

    `)
});

channel.bind('remove-class', (data) => {
    $(`#${data.id}`).empty()
});

$('#confirmation-modal').on('show.bs.modal', function (event) {
    console.log("TEST REMOVAL");
    var button = $(event.relatedTarget); // Button that triggered the modal
    var data_removal_id = button.data('id');
    var data_removal_dept = button.data('dept');
    var data_removal_number = button.data('number');

    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $(this);
    modal.find('.modal-title').text('Deleting ' + data_removal_dept + ' ' + data_removal_number);
    $("#confirm-remove-class-btn").click(function(){ removeSavedClass(data_removal_id); });
})

function removeSavedClass(id) {
    $(function() {
        $.ajax({
            url: "/remove/"+id,
            type: 'DELETE',
            success: function(response) {
                successMessage('Removed Class...');
            },
            error: function(error) {
                errorMessage('Failed Removing Class...');
            }
        });
    });
};

function addClassToProfile(user_id,class_id,csrf_token) {
    $(function() {
        $.ajax({
            type: 'POST',
            url: '/profile/'+user_id+'/add-class',
            data: {class_id: class_id, csrf_token: csrf_token},
            success: function(response) {
                successMessage('Added class...');
            },
            error: function(error) {
                errorMessage('Failed Adding Class...');
            }
        });
    });
}

function removeClassFromProfile(user_id,record_id,csrf_token) {
    $(function() {
        $.ajax({
            url: "/remove-class/"+record_id+"/user/"+user_id,
            type: 'DELETE',
            data: {csrf_token: csrf_token},
            success: function(response) {
                successMessage('Removed Class...');
            },
            error: function(error) {
                errorMessage('Failed Removing Class...');
            }
        });
    });
};


function successMessage(successText) {
    $('.main-content').prepend('<div class="alert alert-success alert-dismissible fade show fixed-top col-6 mx-auto mt-2" role="alert">'
                    + '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
                    + '<span aria-hidden="true">&times;</span> </button>'
                    + '<strong>Success!</strong> '
                    + successText + '</div>');
    setTimeout(function(){
        $(".alert").slideUp(800)
    },5000); 
}

function errorMessage(errorText) {
    $('.main-content').prepend('<div class="alert alert-danger alert-dismissible fade show fixed-top col-6 mx-auto mt-2" role="alert">'
                    + '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
                    + '<span aria-hidden="true">&times;</span> </button>'
                    + '<strong>Error!</strong> '
                    + errorText + '</div>');
    setTimeout(function(){
        $(".alert").slideUp(800)
    },5000); 
}