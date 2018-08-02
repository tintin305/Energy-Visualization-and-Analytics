var nodesG = d3.select('body').append('svg');

var data = {
    nodes: [{
        id: 123,
        x: 20,
        y: 20
    }, {
        id: 456,
        x: 50,
        y: 50
    }]
}

var updateNodes = function (nodes) {
    console.log("updateNodes Called");
    console.log(nodes);
    var node = nodesG.selectAll("circle.node").data(nodes, function (d) {
        return d.id;
    });
    node.enter().append("circle").attr("class", "node")
        .attr("cx", function (d) {
        return d.x
    })
        .attr("cy", function (d) {
        return d.y
    })
        .attr("r", 20)
        .style("fill", "steelblue")
        .style("stroke", "black")
        .style("stroke-width", 1.0);

    node.exit().remove();
}
var update = function () {

    //force.nodes(data.nodes);
    updateNodes(data.nodes);

    //force.links(curLinksData);
    //updateLinks();


    //force.start();
}
update()