// g = new Dygraph(
//     document.getElementById("graph"),
//     // For possible data formats, see http://dygraphs.com/data.html
//     // The x-values could also be dates, e.g. "2012/03/15"
//     `X,Y,Z
//     1,0,3
//     2,2,6
//     3,4,8
//     4,6,9
//     5,8,9
//     6,10,8
//     7,12,6
//     8,14,3`,
//     {
//       // options go here. See http://dygraphs.com/options.html
//       legend: 'always',
//       animatedZooms: true,
//       title: 'dygraphs chart template'
//     });

g = new Dygraph(

  // containing div
  document.getElementById("graphdiv"),

  // CSV or path to a CSV file.
<<<<<<< HEAD
  "/Data/WITS_The_Junction_MSS_3_Kiosk_Sarie_Marais_kVarh.csv",
=======
  // "/Data/WITS_WC_Genmin_LAB_HT_kVArh.csv",
  // "/Data/WITS_WC_Genmin_LAB_HT_kWh.csv",
  // "/Data/WITS_WC_Genmin_LAB_kVarh.csv",
  "/Data/WITS_WC_Genmin_LAB_kWh.csv",
  // "/Data/WITS_WC_Genmin_Sub_kVarh.csv",
  // "/Data/WITS_WC_Genmin_Sub_kWh.csv",
  
>>>>>>> Testing out different functionality with Highmaps and D3.js, I have not got D3.js images to load to the HTML file yet.
  {
  }    // Options


);