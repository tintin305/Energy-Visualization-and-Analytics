$(document).ready(function() {
    var sankey = new Sankey();
  
    sankey.stack(0,["Top","Bottom"]);
    sankey.stack(1,["Merge"]);
    sankey.stack(2,["Good","Bad"]);
  
    sankey.setData([["Top",100,"Merge"],["Bottom",50,"Merge"],["Merge",70,"Good"],["Merge",80,"Bad"]]);
    sankey.draw();
});