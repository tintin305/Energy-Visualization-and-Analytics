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

app.get('/profiles/:DataloggerName/:startDate/:endDate', function(req, res){
    const spawn = require('child_process').spawn;
    const scriptExecution = spawn("python.exe", [(__dirname +"/public/Python_Scripts/DatabaseQuery/DatabaseQuery.py")]);
    
    // Handle normal output
    scriptExecution.stdout.on('data', (data) => {
        console.log(String.fromCharCode.apply(null, data));
    });
 
        // Defining the start date
        var startDate = (req.params.startDate);
        startDate = startDate.replace("%20", "-");
        startDate = startDate.replace("-","/");
        startDate = startDate.replace("-","/");
        client.start(startDate);
    
        // Defining the end date
        var endDate = (req.params.endDate);
        endDate = endDate.replace("%20", "-");
        endDate = endDate.replace("-","/");
        endDate = endDate.replace("-","/");
        client.end(endDate);

    var options = {
        aggregator: 'sum',
        downsample: '5ms-avg',
        rate: 'false',
        metric: req.params.DataloggerName,
        tagKey: 'DataLoggerName',
        tagValue: req.params.DataloggerName,
        host: 'localhost',
        port: 4242,
        ms: 'false',
        arrays: 'true',
        tsuids: 'false',
        annotations: 'none',
        startDate: startDate,
        endDate: endDate
    };

    // Write data (remember to send only strings or numbers, otherwhise python wont understand)
    var data = JSON.stringify(options);
    scriptExecution.stdin.write(data);
    // End data write
    scriptExecution.stdin.end();

        res.sendFile(__dirname + '/Views/DygraphsShow.html');
});

app.get('/index', function(req, res){
    res.sendFile(__dirname + '/Views/DygraphsShow.html');
});

app.get('/HeatMaps', function(req, res){
    PythonShell.run((__dirname +"/public/Python_Scripts/GenerateHeatMap/GenerateHeatMap.py"), function(err){
        if (err) throw err;
            console.log('finished');
            res.sendFile(__dirname + '/Views/HeatMapShow.html');
    });
});

app.get('/ThreeDimensionalView', function(req, res){
    PythonShell.run((__dirname +"/public/Python_Scripts/ThreeDimensionalView/ThreeDimensionalView.py"), function(err){
        if (err) throw err;
            console.log('finished');
            res.sendFile(__dirname + '/Views/ThreeDimensionalViewShow.html');
    });
});

app.get('/DataOutages', function(req, res){
    PythonShell.run((__dirname +"/public/Python_Scripts/DataOutages/DataOutages.py"), function(err){
        if (err) throw err;
            console.log('finished');
            res.sendFile(__dirname + '/Views/DataOutages.html');
    });
});

app.get('/SankeyDiagram', function(req, res){
    const spawn = require('child_process').spawn;
    const scriptExecution = spawn("python.exe", [(__dirname +"/public/Python_Scripts/SankeyGeneration/DatabaseQuery.py")]);
    
    // Handle normal output
    scriptExecution.stdout.on('data', (data) => {
        console.log(String.fromCharCode.apply(null, data));
    });

    var options = {
        aggregator: 'avg',
        downsample: '0all-sum',
        rate: 'false',
        metric: 'WITS_EC_Matrix_Main_Incomer_kWh',
        tagKey: 'DataLoggerName',
        tagValue: 'WITS_EC_Matrix_Main_Incomer_kWh',
        host: 'localhost',
        port: 4242,
        ms: 'false',
        arrays: 'true',
        tsuids: 'false',
        annotations: 'none',
        startDate: '2018/01/01-00:00',
        endDate: '2018/01/07-23:30'
    };

    // Write data (remember to send only strings or numbers, otherwhise python wont understand)
    var data = JSON.stringify(options);
    scriptExecution.stdin.write(data);

    scriptExecution.stderr.on('data', (data) =>{
        console.log(String.fromCharCode.apply(null, data));
    })

    // End data write
    scriptExecution.stdin.end();
    res.sendFile(__dirname + '/Views/SankeyDiagram.html');
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

        var dir = './public/LoggerList';
        if (!fs.existsSync(dir)){
            fs.mkdirSync(dir);
        }
        fs.writeFile("./public/LoggerList/loggerList.csv", metrics, function(err) {
            if(err) {
                return console.log(err);
            }
        });
    });
});

app.listen(3000, function(){
    console.log('Example app listening on port 3000!');
});