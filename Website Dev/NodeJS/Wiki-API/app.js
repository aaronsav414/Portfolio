const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose')
const ejs = require('ejs')

const app = express()

app.set('view engine', 'ejs');
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended: true}));


mongoose.set('strictQuery', false);
mongoose.connect("mongodb://127.0.0.1:27017/wikiDB?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.2", { useNewUrlParser: true });

const articleSchema = {
	title: String,
	content: String
};

const Article = mongoose.model("Article", articleSchema);

// Request all articles

app.route("/articles")

.get(function(req, res){
	Article.find(function(err, foundArticles){
		if (!err) {
			res.send(foundArticles);	
		} else {
			res.send(err);
		}
		
	});

})

.post(function(req, res) {
	const newArticle = new Article({
		title: req.body.title,
		content: req.body.content
	})
	newArticle.save(function(err) {
		if (!err){
			res.send("Successfully added new article.");
		} else {
			res.send(err);
		}
	});
})

.delete(function(req, res) {
	Article.deleteMany(function(err) {
		if (!err){
			res.send("Successfully deleted all articles.");
		} else {
			res.send(err);
		}
	});
});

// Request a specific article

app.route("/articles/:articleTitle")

.get(function(req, res) {

	Article.findOne({ title: req.params.articleTitle }, function(error, results) {
		if (results) {
			res.send(results)
		} else {
			res.send("No articles matching that title was found.")
		}
	})
})

.put(function(req, res){
	Article.updateOne( 
		{ title: req.params.articleTitle }, 
		{ title: req.body.title, content: req.body.content },
		function(err, results) {
		if (results) {
			res.send("Successfully updated article.")
		} else {
			res.send(err)
		}
	})
})

.delete(function (req, res) {
	Article.deleteOne(
		{ title: req.params.articleTitle },
		function(err){
		if (!err){
			res.send("Successfully deleted article.")
		} else {
			res.send(err)
		}
		
	})
})

// Possibly Depricated

// .patch(function(req, res){
// 	Article.updateOne(
// 		{ title: req.params.articleTitle },
// 		{ $set: req.body },
// 		function(err){
// 			if (!err){
// 				res.send("Successfully updated the articles.")
// 			} else {
// 				res.send(err)
// 			}
// 		}
// 	)

// });


// Alternative Method

// app.get("/articles", function(req, res){
// 	Article.find(function(err, foundArticles){
// 		if (!err) {
// 			res.send(foundArticles);	
// 		} else {
// 			res.send(err)
// 		}
		
// 	})

// });

// app.post("/articles", function(req, res) {
// 	const newArticle = new Article({
// 		title: req.body.title,
// 		content: req.body.content
// 	})
// 	newArticle.save(function(err) {
// 		if (!err){
// 			res.send("Successfully added new article.")
// 		} else {
// 			res.send(err)
// 		}
// 	});
// })

// app.delete("/articles", function(req, res) {
// 	Article.deleteMany(function(err) {
// 		if (!err){
// 			res.send("Successfully deleted all articles.")
// 		} else {
// 			res.send(err)
// 		}
// 	})
// })



app.listen(3000, function() {
  console.log("Server started on port 3000.")
});