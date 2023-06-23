var express = require('express')

var app = express()

app.get("/", function(req, res){
  res.send("<h1>Hello</h1>");
});

app.get("/contact", function(req, res){
  res.send("Contact me at: ")
});

app.get("/about", function(req, res){
  res.send("Yo its A a ron")
});

app.get("/hobbies", function(req, res){
  res.send("Camping, Fitness, Sports");
});


app.listen(3000, function() {
  console.log("Server started on port 3000.")
});
