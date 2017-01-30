var graph_c_coor = window.parent.graph_c_coor;

google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(CreateGraphC);

function CreateGraphC() {
      var data = new google.visualization.DataTable();

      data.addColumn('number', 'X');
      data.addColumn('number', 'Y');
      data.addRows(graph_c_coor);

      var options = {
        hAxis: {
          title: 'X axis'
        },
        vAxis: {
          title: 'Y axis'
        }
      };

      var chart = new google.visualization.ScatterChart(document.getElementById('partC'));
      chart.draw(data, options);

    }





