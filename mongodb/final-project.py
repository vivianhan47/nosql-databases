# Put the use case you chose here. Then justify your database choice:
# Answer: 
# A hackernews website could be set up using mongodb database 
# since mongodb is great for storing variable format records 
# and could wrap other models within a main model - user.
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# Information on that specific server could not be displayed,
# 
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
#
#


import pymongo
import datetime
from pymongo import MongoClient
from pprint import pprint
from bson.binary import Binary

# client = MongoClient("mongodb://localhost")

# if 'hackernews' in client.database_names():
# 	drop_database('hackernews')

# # Create a database named "hackernews"
# db = client.hackernews

# Three users:
# lily, kim, alex

# fifteen objects:
# 2 articles.
# 2 comments.
# 2 shows.
# 1 ask.
# 2 messages.
# 2 jobs.
# 4 votes.

# Table 1: user. 
def create_user(db):
	db.user.insert_many([
		{"username": "lily","password": "password",},
		{"username": "kim","password": "password",},
		{"username": "alex","password": "password",}
	])

# insert articles
# Table 2: article.
def create_article(db):
	db.article.insert_many([
		{"author": "lily",
		"ID": 1,
		"title": "What happens before main() function is executed in C and why is it important?",
		"link": "http://mymicrocontroller.com/2018/04/03/what-happens-before-main-function-is-executed-in-c-and-why-is-it-important/",
		"votes": 100,
		"date_posted": 20180403,
		"keyword": ["C", "main"],
		},
		{"author": "kim",
		"ID": 2,
		"title": "Yale physicists find signs of a time crystal",
		"link": "https://news.yale.edu/2018/05/02/yale-physicists-find-signs-time-crystal",
		"votes": 147,
		"date_posted": 20180502,
		"keyword": ["time", "crystal", "physics"],
		}
	])

# insert comments
# Table 3: comment.
def create_comment(db):
	db.comment.insert_many([
		{"user": "alex",
		"content": "awesome",
		"location_ID": 1,
		"location_type": "article",
		"date_posted": 20180501,
		},
		{"user": "lily",
		"content": "thanks",
		"location_ID": 2,
		"location_type": "show",
		"date_posted": 20180420,
		}
	])

# insert shows
# Table 4: show.
def create_show(db):
	db.show.insert_many([
		{"user": "alex",
		"ID": 1,
		"title": "A color-accurate Instagram-like filters reconstruction for apps",
		"link": "https://github.com/homm/color-filters-reconstruction#accurate-instagram-filters-reconstruction",
		"votes": 99,
		},
		{"user": "kim",
		"ID": 2,
		"title": "A CSS Grid generator for building layouts faster",
		"link": "https://www.layoutit.com/grid",
		"votes": 50,
		}
	])

# insert ask
# Table 5: ask.
def create_ask(db):
	db.ask.insert_one(
		{"user": ["kim", "lily"],
		"ID": 1,
		"title": "Startup to enterprise and back to startups, how?",
		"message": {
			"1": {"user": "kim", "content": "some comment",},
			"2": {"user": "lily", "content": "okay",}
			}
		}
	)

# insert messgae
# Table 6: message.
def create_message(db):
	db.message.insert_many([
		{"sender": "lily",
		"receiver": "alex",
		"content": "hi",
		},
		{"sender": "lily",
		"receiver": "kim",
		"content": "hello",
		}
	])

# insert jobs
# Table 7: job.
def create_job(db):
	db.job.insert_many([
		{"user": "lily",
		"ID": 1,
		"title": "Sendwithus (YC W14) Is Hiring a Product Owner in Victoria BC",
		"link": "https://www.sendwithus.com/careers/e180f0b2-036e-4842-bd65-cbbaa2e8650f",
		"closed": 0,
		},
		{"user": "kim",
		"ID": 2,
		"title": "New Story (YC S15 nonprofit) is hiring a Videographer",
		"link": "https://newstorycharity.org/careers/videographer/",
		"closed": 0,
		}
	])

# insert votes
def create_vote(db):
	db.vote.insert_many([
		{"user": "alex",
		"content_ID": 2,
		"content_type": "show",

		},
		{"user": "kim",
		"content_ID": 1,
		"content_type": "show",

		},
		{"user": "kim",
		"content_ID": 1,
		"content_type": "article",

		},
		{"user": "lily",
		"content_ID": 2,
		"content_type": "article",

		}
	])

# Bill is a new programmer who is looking forward to join the hackernews community to improve
# his coding skills.

# First of all, Bill creates his account.
# Action 1: A user signs up for an account
def action_sign_up(db, username="bill", password="bill_is_swag"):
	db.user.insert_one(
		{"username": username,
		"password": password}
	)

# Then, Bill publishes an article, try to play around with the forum.
# Action 2: A user publishes an article
def action_publish_article(db, article_title="a new post", article_link="something", username="bill", ID=3):
	date = datetime.datetime.now().strftime("%Y%m%d")
	db.article.insert_one(
		{"author": username,
		"ID": ID,
		"title": article_title,
		"link": article_link,
		"votes": 0,
		"date_posted": date,
		"keyword": [],
		}
	)

# After creating the article, Bill wants to delete the useless article.
# Action 3: A user deletes an article
def action_delete_article(db, article_title="a new post", username="bill", ID=3):
	if ID:
		db.article.remove({"ID": ID})
	if article_title and username:
		db.article.remove({"article_title": article_title, "username": username})


# Bill saw some really good articles, he then up-votes the article.
# Action 4: A user up-votes an article given the article id
def action_up_votes(db, content_id=3, content_type="article", user="bill"):
	voted = db.vote.find({"user": user, "content_ID": content_id})
	if not voted.count():
		db.vote.insert_one(
			{"user": user,
			"content_ID": content_id,
			"content_type": content_type,
			})
		if content_type == "article":
			db.article.update(
				{"ID": content_id}, 
				{"$inc": {"votes": 1}}
			)
		elif content_type == "show":
			db.show.update(
				{"ID": content_id}, 
				{"$inc": {"votes": 1}}
			)

# Bill misclicked the wrong article to upvote. He then downvoted the article.
# Actuib 5: A user can down-votes an article given the article id, if he has voted before.
def action_down_votes(db, content_id=3, content_type="article", user="bill"):
	voted = db.vote.find({"user": user, "content_ID": content_id})
	if voted.count():
		db.vote.remove(
			{"user": "alex",
			"content_ID": content_id,
			"content_type": content_type,
			})
		if content_type == "article":
			db.article.update(
				{"ID": content_id}, 
				{"$inc": {"votes": -1}}
			)
		elif content_type == "show":
			db.show.update(
				{"ID": content_id}, 
				{"$inc": {"votes": -1}}
			)

# Bill want to see the best 10 articles in the forum to learn new materials in the most efficinet way.
# Action 6: list of 10 highest-voted articles
def action_10_highest_voted_articles(db):
	ten_articles=db.article.aggregate([
		{"$sort": {"votes": -1}},
		{"$limit": 10}
	])
	for element in ten_articles:
		pprint(element)

# Bill finds out all articles that are published before the given date.
# Action 7: Get all articles posted prior to a certain date
def action_articles_before(db, date=20180504):
	articles_before = db.article.find(
		{"date_posted": {"$lt": date}},
	)
	for element in articles_before:
		pprint(element)

# Bill finds out all articles that are published after the given date.
# Action 8: Get all articles posted after a certain date
def action_articles_after(db, date=19990101):
	articles_before = db.article.find(
		{"date_posted": {"$gt": date}},
	)
	for element in articles_before:
		pprint(element)





