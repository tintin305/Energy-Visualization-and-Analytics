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


g1 = new Dygraph(
  // containing div
  document.getElementById("graphdiv3"),
  // CSV or path to a CSV file.
  "Date,Temperature\n" +
  "2008-05-07,75\n" +
  "2008-05-08,70\n" +
  "2008-05-09,80\n"
);
g2 = new Dygraph(
  // containing div
  document.getElementById("graphdiv4"),
  // CSV or path to a CSV file.
  "Date,Temperature\n" +
  "2008-05-07,80\n" +
  "2008-05-08,75\n" +
  "2008-05-09,70\n"
);
$(document).ready(function(){
$(".profiles").find(".tab").hide();
$(".profiles").find(".tab").first().show();
$(".profiles").find(".tabs li").first().find("a").addClass("active");
  //click handler for tabbing
  $(".profiles").find(".tabs").find("a").click(function(){
      tab = $(this).attr("href");
      $(".profiles").find(".tab").hide();
      $(".profiles").find(".tabs").find("a").removeClass("active");
      $(tab).show();
      $(this).addClass("active");
      //start new code
      if(tab == "#graphdiv1")
          g1.resize();
      else
          g2.resize();
      //end new code
      return false;
  });
});
