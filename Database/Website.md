---
title: Web Server Notes
---

There way be a way in which to query the database such that it can downsample each day into a specific number of samples.
This allows for the use of the Highgraphs package. 
The Highgraphs package seems to be the easiest to use as it can take data directly from the JSON and edit that.

A method that can be used for dygraphs is:
    First request the meter, then edit it into a csv type (https://stackoverflow.com/questions/29954146/how-to-create-a-csv-file-on-the-server-in-nodejs)

    Then once this has been converted, store it as a temporary file on the ((server/client)?)
    This can then be called in the js file that is used to create the dygraphs (https://en.proft.me/2016/06/16/how-create-temporary-file-nodejs/).



It appears as if the issue with D3.js is that the files that it creates is in a SVG format, this is not readable by the HTML page.
It appears as if Snap.svg may be useful for this problem, it also seems to allow all kinds of other fancy stuff to happen.
Another way around this is to generate the image on the server side, then once this has happened, send a converted version of this SVG to the HTML to render.


I believe that there is a way to get the data out of the JSON directly with the use of either parsing it, or getting out the required parameter that extracts the data. 
This should make things faster than the way we are doing it currently. 

# The Sankey Diagram

The idea behind the Sankey diagram is such that one needs to map a tree diagram of the system which starts from the incomer, then flows down to each of the individual loads on that subsystem.
In order to do this, a system should be generated such that the data drawn from the database needs to sum the values from a specific time range. The request will be made from multiple metrics at the same time. These metrics will be the dataloggers which make up the system.

There appears to be some sort of functionality for achieving this summing function. 
The first method is to make use of downsampling, this will give an idea of the average magnitude of the energy used over a period. 
One can select downsampling and specify the interval to downsample to be the entire date range specified. The command "all" will do this.

For simplicity, I am going to start with the matrix as this has a main incomer, a generator, and many buildings which make it up.

When using the Node.js quering system, it is unable to understand the 0all-sum query. 
However, when I put the query directly into the url of a browser, it understands the query and returns the exact requested numbrs:
    http://localhost:4242/api/query?ms=false&arrays=false&show_tsuids=false&no_annotations=true&global_annotations=false&start=2018/01/01%2000:00&end=2018/01/08%2000:00&m=avg:0all-sum:WITS_EC_Matrix_Main_Incomer_kWh{DataLoggerName=WITS_EC_Matrix_Main_Incomer_kWh}

The OpenTSDB GUI also has an issue with downsampling the entire date range using the "0all-sum" term, so this can be something to raise on the OpenTSDB on GitHub.  