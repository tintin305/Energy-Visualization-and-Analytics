  g = new Dygraph(

    // containing div
    document.getElementById("graphdiv"),
  
    // CSV or path to a CSV file.
    "/tmp/temp.csv",
    // {
      // axis : {
      //   x : {
      //     valueFormatter: Dygraph.dateString_,
      //     valueParser: function(x) { return 1000*parseInt(x); },
      //     ticker: Dygraph.dateTicker                
      //   }
      // }
    // }
  {
    // xRangePad: 10,
    // yRangePad: 10,
    // xValueFormatter: Dygraph.dateString_,
    // xValueParser: function (x){
    //   return 1000 * parseInt(x, 10);
    // },
    // xTicker: Dygraph.dateTicker,
    // labels: ["Dates", "Not Kept", "Hosts"],
    // title: "Promises not kept",
    // legend: "always",
    // drawPoints: "true",
    // pointSize: 2,
    // colors: ["orange", "blue", "black"],
    // strokeWidth: 1
 
  }
  );
