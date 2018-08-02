    /* Define an array of objects */

    var data = [];
    for(var i=0; i<240; i++) data[i] = {title: "Segment "+i, value: Math.round(Math.random()*100)};
    

    /* Define an accessor function */
    chart.accessor(function(d) {return d.value;})
    
    d3.select('#chart4')
        .selectAll('svg')
        .data([data])
        .enter()
        .append('svg')
        .call(chart);
    
    /* Add a mouseover event */
    d3.selectAll("#chart4 path").on('mouseover', function() {
        var d = d3.select(this).data()[0];
        console.log(d.title + ' has value ' + d.value);
    });