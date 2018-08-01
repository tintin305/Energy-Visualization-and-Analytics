const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
const app = express();

// OpenTSDB Package
var opentsdb = require( 'opentsdb' );
var client = require('opentsdb-client')();
// var client = opentsdb.client();
var mQuery = require('opentsdb-mquery')();
// const apiKey = '*****************';

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
  // res.send('This will be to get a dataloggers JSON ' + req.params.DataloggerName)
  res.render('newThing', {passing: req.params.DataloggerName})
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
  

})

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
})
