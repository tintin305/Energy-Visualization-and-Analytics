function csvJSON(csv){
            // console.log(data);
    var lines=csv.split("\n");
  
    var result = [];
    // console.log(lines[0]);
    
    var headers=lines[0].split(",");
  

    for(var i=1;i<lines.length;i++){
        var obj = {};
        var currentline=lines[i].split(",");
        obj[currentline[0]] = currentline[1];
        result.push(obj);
        // console.log(obj)
    }
    //return result; //JavaScript object
    return JSON.stringify(result); //JSON
  
    }
    


// var fs = require('fs');
// var readStream = fs.createReadStream(__dirname + '/tmp/temp.csv', 'utf8');

// let data = ''
// readStream.on('data', function(chunk) {
//    data += chunk;
// }).on('end', function() {
//      out = csvJSON(data)
   
//     console.log(JSON.stringify(out))
// });