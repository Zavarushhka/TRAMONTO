function updateTable() {
    $.ajax({
        url: '/get_data/',
        dataType: 'json',
        success: function(data) {
            updateTableData(data);
        }
    });
}

function updateTableData(data) {
    var table = document.getElementById('table');
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }
    console.log(data)
    for (var i = 0; i < data.length; i++) {
       var newRow = table.insertRow(table.rows.length);
       newRow.insertCell(0).innerHTML = i + 1;
       newRow.insertCell(1).innerHTML = data[i].nickname;
       }
}

setInterval(updateTable, 5000);