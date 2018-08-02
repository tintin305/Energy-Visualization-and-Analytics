const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const app = express();

// OpenTSDB Package
var opentsdb = require( 'opentsdb' );
var client = require('opentsdb-client')();
// var client = opentsdb.client();
var mQuery = require('opentsdb-mquery')();

// D3 Package
var d3 = require('d3');
var jsdom = require('jsdom');

// To export JSON to csv
var jsonexport = require('jsonexport');
var fs = require('fs');

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

// This will link up the javascript files that are called in the HTML file
app.get('/js/', function(req, res){
  res.sendFile(__dirname + '/js/');
});

// This will get the value put in the dropdown box
app.get('/getJson', function (req, res) {
  // If it's not showing up, just use req.body to see what is actually being passed.
  console.log(req.body.selectpicker);
});



// app.get('/js/index2.js', function(req, res){
  // res.sendFile(__dirname + '/js/index2.js');
// });

app.get('/', function (req, res) {
  res.render('index', {weather: null, error: null});
})

app.get('/profiles/:DataloggerName', function(req, res){
  //download temp file here
  var end = Date.now();
  var start = end - 100;

  mQuery.aggregator('sum');
  mQuery.downsample('5m-avg');
  mQuery.rate(false);
  mQuery.metric(req.params.DataloggerName);
  mQuery.tags('DataLoggerName', req.params.DataloggerName);
client.host('localhost');
client.port(4242);
client.ms(false);
client.tsuids(false);
client.annotations('none');
// client.start( start );
client.start('2013/01/01 01:00');
client.end('2018/05/05 01:00');
// client.arrays(false);
// client.end( end );
client.queries( mQuery );
var url = client.url();
client.get( function onData(error, data) {
    if (error){
      console.error( JSON.stringify(error));
      return;
    }
    console.log(url);
    console.log( data);
    var dir = './tmp';

if (!fs.existsSync(dir)){
    fs.mkdirSync(dir);
}
//not exporting properly:
    jsonexport(data, {rowDelimiter: '\t'},function(err, csv){
    fs.writeFile("./tmp/test.csv", csv, function(err) {
    if(err) {
      console.log(err)
    }
    });
 });
  // console.log(JSON.stringify(data.dps))
  });
  

  res.render('newThing', {passing: req.params.DataloggerName});
  
})

app.get('/D3Test', function(req, res){
  res.render('D3Test');
})

app.get('/HighMapTest', function(req, res){
  res.render('HighMapTest');
})



app.get('/D3RadialMap', function(req, res){
  res.render('D3RadialMap');
})


app.get('/HeatMapD3', function(req, res){
  res.render('HeatMapD3', testing);
})



// app.get('/', function (req, res) {
//   client.host('localhost');
// client.port(4242);
// client.ms( false );

// client.metrics( function onResponse( error, metrics ) {
//   if ( error ) {
//       console.error( JSON.stringify( error ) );
//       return;
//   }
//   res.send('This is the list of metrics on the database' + JSON.stringify( metrics ) );
//   console.log( JSON.stringify( metrics ) );
// });
// })


//https://www.npmjs.com/package/opentsdb

// When the user enters 'localhost:3000/metrics/' then the server will query the database and return a list of metrics to the log and to the web page.
app.get('/metrics/', function(req, res){
  // res.send('This is the list of metrics on the database' + req.params.DataloggerName)

client.host('localhost');
client.port(4242);
client.ms( false );

client.metrics( function onResponse( error, metrics ) {
  if ( error ) {
      console.error( JSON.stringify( error ) );
      return;
  }
  // res.send('This is the list of metrics on the database' + JSON.stringify( metrics ) );
  // console.log( JSON.stringify( metrics ) );
  res.render('things',{lists: metrics }) 
});
})

app.get('/WITS_WC_Genmin_Sub_kVarh/', function(req, res){
  var end = Date.now();
  var start = end - 100;

  mQuery.aggregator('sum');
  mQuery.downsample('5m-avg');
  mQuery.rate(false);
  mQuery.metric('WITS_WC_Genmin_Sub_kVarh');
  mQuery.tags('DataLoggerName', 'WITS_WC_Genmin_Sub_kVarh');
client.host('localhost');
client.port(4242);
client.ms(false);
client.tsuids(false);
client.annotations('none');
// client.start( start );
client.start('2013/01/01 01:00');
client.end('2018/05/05 01:00')
// client.end( end );
client.queries( mQuery );
var url = client.url();
client.get( function onData(error, data) {
    if (error){
      console.error( JSON.stringify(error));
      return;
    }
    console.log(url);
    console.log( JSON.stringify(data));
  });
  

});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
});