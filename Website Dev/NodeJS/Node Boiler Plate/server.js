const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
const ejs = require('ejs')

// Express
const app = express()

// EJS
app.set('view engine', 'ejs');
app.use(express.static("public"));

// BodyParser
app.use(bodyParser.urlencoded({extended: true}));

// Mongoose
mongoose.set('strictQuery', false);
mongoose.connect("mongodb://localhost:27017/dbName", { useNewUrlParser: true });


app.get("/", function(req, res){
  res.send("Hello World!");
})


app.listen(3000, function() {
  console.log("Server started on port 3000.")
});
