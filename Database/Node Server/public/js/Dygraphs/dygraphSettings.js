g = new Dygraph(
    document.getElementById("graphdiv"),
        "/tmp/temp.csv",
        {
            axes: {
            x : {
            valueFormatter: Dygraph.dateString_,
            ticker: Dygraph.dateTicker
            }
            },
            legend: "always"
        }
);