const express = require("express");
const https = require("https");
const bodyParser = require("body-parser")

const app = express();

app.use(bodyParser.urlencoded({extended: true}));


app.get("/", function(req, res){
  res.sendFile(__dirname + "/index.html")
});

app.post("/", function(req, res){

  const query = req.body.cityName
  const appid = "d3bf2a03b2877faeab2c11a679d77a60"
  const units = "metric"
  const url = "https://api.openweathermap.org/geo/1.0/direct?q=" + query + "&limit=5&appid=" + appid + "&units=" + units


  https.get(url, function(response){
    console.log(response);

    response.on("data", function(data){
      const weatherData = JSON.parse(data);
      const temp = weatherData.main.temp;
      const weatherDescription = weatherData.weather[0].description //Use JSON Viewer Pro on Chrome
      const icon = weatherData.weather[0].icon
      const imageURL = "https://openweathermap.org/img/wn/" + icon + "@2x.png"
      res.write("<p>The weathe is currently " + weatherDescription + "</p>");
      res.write("<h1>The temperature in " + query + "is " + temp + " degrees Celcius</h1>");
      res.write("<img src=" + imageURL + ">")
      res.send()

    });

  });

});




app.listen(3000, function(){
  console.log("Server started on port 3000")
});
