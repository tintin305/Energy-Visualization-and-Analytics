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


