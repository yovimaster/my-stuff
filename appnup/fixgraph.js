window.onload = function () {
    var Newarr = []
          var chart = new CanvasJS.Chart("chartContainer", {
      title:{
        text: "Rendered on spot chart"                    
      },
      axisX: {
        maximum: 10,
        minimum: 0,
        gridThickness: 1,
	      tickThickness: 1,
        gridColor: "lightgrey",
        tickColor: "lightgrey",
        lineThickness: 0
      },
      axisY:{
        title: "Y axis",              
        gridThickness: 1,
	tickThickness: 1,
        gridColor: "lightgrey",
        tickColor: "lightgrey",
        lineThickness: 0,
        maximum: 100,
        interval: 10
        
      },

      data: [
      {        
        type: "bubble",     
        toolTipContent: "<span style='\"'color: {color};'\"'><strong>{label}</strong></span><br/> <strong>Number of FU</strong> {x} per year <br/> <strong>Fixed </strong> {y} mistakes<br/>",
        dataPoints: Newarr
      }
      ]
    });
  function renderNow() {
                xValue = parseFloat(document.getElementById("xval").value);
                yValue = parseFloat(document.getElementById("yval").value);
                zValue = parseFloat(document.getElementById("zval").value);
                label = document.getElementById("label").value;
                Newarr.push({
                    x: xValue,
                    y: yValue, 
                    z: zValue,
                    label: label
                });
                chart.render();
            }

            var renderButton = document.getElementById("renderButton");
            renderButton.addEventListener("click",function(event){
                                                    event.preventDefault();
                                                    renderNow();
       }); 
}