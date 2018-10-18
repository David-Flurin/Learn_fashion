var express = require('express');
var fileUpload = require('express-fileupload');
var app = express();
var spawn = require('child_process').spawn;
var path = "images/filename.jpg";
var args = ["predict_it.py", path];

app.use(fileUpload());
app.use(express.static('public'));


app.get('/index.htm', function (req, res) {
   res.sendFile( __dirname + "/" + "index.htm" );
})

app.post('/', function (req, res) {
   let sampleFile = req.files.upload;
 
  // Use the mv() method to place the file somewhere on your server
  sampleFile.mv(path, function(err) {
    if (err)
      return res.status(500).send(err);
 
  });
  var myCommand = spawn("python", args);

  myCommand.stdout.on('data', function(data){
  	//res.send(data);
  	console.log(data.toString());
  	res.send(data.toString());
  })

  myCommand.stderr.on('data', function(data){
  	console.log("Not successful");
  	console.log(data.toString());
  })
   
   
})

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("Example app listening at http://%s:%s", host, port)
})