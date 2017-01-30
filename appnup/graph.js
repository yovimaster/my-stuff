// In this Home work i choosed google graph, Because documantation wise and visual wise it is the best library I've seen
//For each part in the assignment I've created a graph for it, Graph A, Graph B and graph C
google.charts.load('current', {packages: ['corechart', 'line']});
google.charts.setOnLoadCallback(CreateGraphA);
// This function Gets the Json data, and because of the synchronise of JS, i call it before the graph is being created
jsondata();
google.charts.setOnLoadCallback(CreateGraphB);


///////////////////////////////////////////////////////////////////////////
////////////////////// part A               ///////////////////////////////
///////////////////////////////////////////////////////////////////////////
function CreateGraphA() {
      var data = new google.visualization.DataTable();
      var coordinates = [[3,6], [9,1], [7,8], [4,5], [45,0], [36,1]]

      data.addColumn('number', 'X');
      data.addColumn('number', 'Y');
      data.addRows(coordinates);

      var options = {
        hAxis: {
          title: 'X axis'
        },
        vAxis: {
          title: 'Y axis'
        }
      };

      var chart = new google.visualization.ScatterChart(document.getElementById('partA'));
      chart.draw(data, options);
    }

///////////////////////////////////////////////////////////////////////////
////////////////////// part B               ///////////////////////////////
///////////////////////////////////////////////////////////////////////////

var graph_b_coor =[]
function jsondata() {
        $.getJSON("http://www.mocky.io/v2/588f1d893f00003017dde3a7", function(jason){
        $.each(jason, function (key, data) {
          $.each(data, function (index, data) {
              graph_b_coor.push([data["x"],data["y"]]);
          });
        }); 
      });
 }

function CreateGraphB() {
      var data = new google.visualization.DataTable();

      data.addColumn('number', 'X');
      data.addColumn('number', 'Y');
      
      data.addRows(graph_b_coor);

      var options = {
        hAxis: {
          title: 'X axis'
        },
        vAxis: {
          title: 'Y axis'
        }
      };

      var chart = new google.visualization.ScatterChart(document.getElementById('partB'));
      chart.draw(data, options);

    }


///////////////////////////////////////////////////////////////////////////
////////////////////// part C               ///////////////////////////////
///////////////////////////////////////////////////////////////////////////
var graph_c_coor = []
function add_point(){
  x = parseFloat(document.getElementById("xval").value);
  y = parseFloat(document.getElementById("yval").value);
  graph_c_coor.push([x,y]);
  document.getElementById('graphc').contentDocument.location.reload(true);
}
   