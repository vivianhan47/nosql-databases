import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost")
db = client.movie_db
collection = db.movie_collection

# Part A
collection.update_many(

		{"rated": "NOT RATED", "genres": "Comedy"},
		{"$set":{"rated": "Pending rating"}}
)

#Part B

collection.insert_one({
	"title": "Despicable Me",
	"year": 2010,
	"countries":["USA","France"],
	"genres":["Animation", "Adventure", "Comedy", "Family", "Fantasy"],
	"directors":["Pierre Coffin", "Chris Renaud"],
	"imdb":{
		"id": 1323594,
		"rating": 7.7,
		"votes": 435255,
	}
	
});


#Part C
comedy = collection.aggregate([
		{"$match" : {"genres": "Comedy"}},
		{"$group" : {"_id": "Comedy", "count": {"$sum": 1}}}
	])
for element in comedy:
	pprint(element)


#Part D
country = collection.aggregate([
		{"$match" : {"countries": "China", "rated": "Pending rating"}},
		{"$group" : {"_id": {"country": "China", "rating": "Pending rating"}, 
					"count": {"$sum": 1}}}

	])
for element in country:
	pprint(element)


#Part E
db.TV.insert_many([
		{"title": "Game of Thrones",
		"year": 2011,
		"countries":["USA","UK"],
		"genres":["Action", "Adventure", "Drama", "Fantasy", "Romance"],
		
		"id": "0944947",
	
		},
		{"title": "Westworld",
		"year": 2016,
		"countries":["USA"],
		"genres":["Mystery", "Sci-Fi", "Western", "Drama"],
		
		"id": "0475784",
			
		}
	])

db.TVimdb.insert_many([
		{
		"id": "0944947",
		"rating": 9.5,
		"votes": 1310157,
		},
		{
		"id": "0475784",
		"rating": 8.9,
		"votes": 267330,
		}
	])


lookup = db.TV.aggregate([{"$lookup" : {
		"from": "TVimdb",
		"localField": "id",
		"foreignField": "id",
		"as": "imdb_rating"
	}
}])

for element in lookup:
	pprint(element)



