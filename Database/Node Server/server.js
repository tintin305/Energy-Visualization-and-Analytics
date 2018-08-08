const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const app = express();

// OpenTSDB Package
var opentsdb = require( 'opentsdb' );
var client = require('opentsdb-client')();
var mQuery = require('opentsdb-mquery')();

// D3 Package
var d3 = require('d3');
var jsdom = require('jsdom');

// To export  to csv
var fs = require('fs');


//Running Python
var PythonShell = require('python-shell');


app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

// This will link up the javascript files that are called in the HTML file
app.get('/js/', function(req, res){
    res.sendFile(__dirname + '/js/');
});

app.get('/', function (req, res){
    res.sendFile(__dirname + '/Views/index.html');
})

// 
app.get('/profiles/:DataloggerName/:startDate/:endDate', function(req, res){
    mQuery.aggregator('sum');
    mQuery.downsample('5ms-avg');
    mQuery.rate(false);
    mQuery.metric(req.params.DataloggerName);
    mQuery.tags('DataLoggerName', req.params.DataloggerName);
    client.host('localhost');
    client.port(4242);
    client.ms(false);
    client.tsuids(false);
    client.annotations('none');

    // Defining the start date
    var startDate = (req.params.startDate);
    startDate = startDate.replace("%20", " ");
    startDate = startDate.replace("-","/");
    startDate = startDate.replace("-","/");
    client.start(startDate);

    // Defining the end date
    var endDate = (req.params.endDate);
    endDate = endDate.replace("%20", " ");
    endDate = endDate.replace("-","/");
    endDate = endDate.replace("-","/");
    client.end(endDate);

    client.arrays(false);
    client.queries(mQuery);
    var url = client.url();
    client.get(function onData(error, data){
        if (error){
            console.error( JSON.stringify(error));
            return;
        }
        OGstring = JSON.stringify(data)
        dataString = OGstring.replace("]", " ");
        newstring = dataString;
        newstring = newstring.replace(/\],\[/g, '\n');
        dataIndex = newstring.indexOf('[[')
        newstring = newstring.substring(dataIndex+2)

        //  Remove unwanted brackets 
        newstring = newstring.replace(/\]/g, '');
        newstring = newstring.replace(/\}/g, '');
        // newstring = newstring.replace(/000,/g, ',');

        // NB //
        // Test if this works properly
        newstring = "Timestamp, " + req.params.DataloggerName   + "\n" + newstring;


        var dir = './public/tmp';
        if (!fs.existsSync(dir)){
            fs.mkdirSync(dir);
        }
        fs.writeFile("./public/tmp/temp.csv", newstring, function(err) {
        if(err) {
            return console.log(err);
        }
        console.log("The file was saved!");
        res.sendFile(__dirname + '/Views/DygraphsShow.html');
        }); 
    });
});

app.get('/index', function(req, res){
    res.sendFile(__dirname + '/Views/DygraphsShow.html');
});

app.get('/HeatMaps', function(req, res){
PythonShell.run((__dirname +"/public/Python_Scripts/GenerateHeatMap.py"), function(err){
    if (err) throw err;
        console.log('finished');
        res.sendFile(__dirname + '/Views/HeatMapShow.html');
});

});

// When the user enters 'localhost:3000/metrics/' then the server will query the database and return a list of metrics to the log and to the web page.
app.get('/metrics/', function(req, res){
    client.host('localhost');
    client.port(4242);
    client.ms(false);
    client.metrics(function onResponse(error, metrics){
        if (error) {
            console.error( JSON.stringify(error));
            return;
        }
    res.render('logger_list',{lists: metrics }); 
    });
})

app.listen(3000, function(){
    console.log('Example app listening on port 3000!');
});