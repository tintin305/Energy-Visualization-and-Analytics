$(document).ready(function(){
	$('<div class="test"/>').insertBefore('canvas:nth-child(4)');
	$('.dygraph-rangesel-zoomhandle').removeAttr('src');
	//getFormatedData(dataArray);



function getFormatedData(dataArray) {
		  var r = "reportDate,Received,Transmitted,High Utilization Threshold\n";
		  for (var i = 0; i < dataArray.length; i++) {
		      r += dataArray[i].reportDate;		      
		      r += "," + dataArray[i].maxRxOct;
			  r += "," + dataArray[i].maxTxOct;
		      r += "," + portSpeed;
		      r += "\n";
		  }
		  console.log(r);
		  return r;
		}
		var portSpeed = 819.2;
		var data1;
		$.getJSON("data.json", function (data) {
		    data1 = data;

		    data1 = getFormatedData(data1);

		var g1 = new Dygraph(document.getElementById("demodiv"), data1, {
			  //title: 'Utlization Loews',
			 
			  
			  stackedGraph: false,
              labelsDiv: document.getElementById("labels"),
			  ylabel:"Bandwidth (Kbps)",
			  xlabel:"Days (GMT)" , 
			  legend: 'always' ,
			  showRangeSelector: true,
			  drawPoints: false,
			  colors: ['#e7cf79','#95bed4','#cd040b'],		  
			  fillGraph: true,
		      fillAlpha: 0.9,	
			  rangeSelectorHeight: 50,
			  rangeSelectorPlotFillColor: '#cd040b',
			  showRoller :false,
			  labelsSeparateLines: true,
		      rangeSelectorPlotFillGradientColor: '',
			//  rangeSelectorAlpha: 0.1,
			//  rangeSelectorPlotStrokeColor: 'white',
			//  rangeSelectorBackgroundStrokeColor: 'black',
			//  rangeSelectorBackgroundLineWidth: 1,
			//  rangeSelectorPlotLineWidth: 1,
			//  rangeSelectorForegroundStrokeColor: '#ffffff',
			//  rangeSelectorForegroundLineWidth: false,
		    //  rangeSelectorAlpha: 0.5,
			});
		});
		
});