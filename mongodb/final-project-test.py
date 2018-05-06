import pymongo
import datetime
from pymongo import MongoClient
from pprint import pprint
from bson.binary import Binary
from final_project import *

client = MongoClient("mongodb://localhost")

print("connected")

if "hackernews" in client.database_names():
	client.drop_database('hackernews')

print("if database exists, drop database")

# Create a database named "hackernews"
db = client.hackernews


def create_user_test():
	create_user(db)
	res = db.user.find()
	for ele in res:
		pprint(ele)

def create_article_test():
	create_article(db)
	res = db.article.find()
	for ele in res:
		pprint(ele)

def create_comment_test():
	create_comment(db)
	res = db.comment.find()
	for ele in res:
		pprint(ele)

def create_show_test():
	create_show(db)
	res = db.show.find()
	for ele in res:
		pprint(ele)

def create_ask_test():
	create_ask(db)
	res = db.ask.find()
	for ele in res:
		pprint(ele)

def create_message_test():
	create_message(db)
	res = db.message.find()
	for ele in res:
		pprint(ele)

def create_job_test():
	create_job(db)
	res = db.job.find()
	for ele in res:
		pprint(ele)

def create_vote_test():
	create_vote(db)
	res = db.vote.find()
	for ele in res:
		pprint(ele)

def sign_up_test():
	print("\nbefore sign up\n")
	res = db.user.find()
	for ele in res:
		pprint(ele)
	action_sign_up(db)
	print("\nafter sign up\n")
	res = db.user.find()
	for ele in res:
		pprint(ele)

def publish_article_test():
	print("\nbefore publish article\n")
	res = db.article.find()
	for ele in res:
		pprint(ele)
	action_publish_article(db)
	print("\nafter publish article\n")
	res = db.article.find()
	for ele in res:
		pprint(ele)

def delete_article_test():
	print("\nbefore delete article\n")
	res = db.article.find()
	for ele in res:
		pprint(ele)
	action_delete_article(db, ID=1)
	print("\nafter delete article\n")
	res = db.article.find()
	for ele in res:
		pprint(ele)

def up_vote_test():
	print("\nbefore up vote article 1\n")
	res = db.article.find({"ID": 1})
	for ele in res:
		pprint(ele)
	print("##############################")
	res2 = db.vote.find({"user": "Bill"})
	for ele in res2:
		pprint(ele)
	print("##############################")
	action_up_votes(db, content_id=1, user="bill")
	print("\nafter up vote article\n")
	res = db.article.find({"ID": 1})
	for ele in res:
		pprint(ele)
	print("##############################")
	res2 = db.vote.find({"user": "Bill"})
	for ele in res2:
		pprint(ele)

def down_vote_test():
	print("\nbefore down vote show 1\n")
	res = db.show.find({"ID": 2})
	for ele in res:
		pprint(ele)
	print("##############################")
	res2 = db.vote.find({"user": "alex"})
	for ele in res2:
		pprint(ele)
	print("##############################")
	action_down_votes(db, content_id=2, content_type="show", user="alex")
	print("\nafter down vote show\n")
	res = db.show.find({"ID": 2})
	for ele in res:
		pprint(ele)
	print("##############################")
	res2 = db.vote.find({"user": "alex"})
	for ele in res2:
		pprint(ele)

def ten_highest_test():
	print("##############################")
	action_10_highest_voted_articles(db)

def articles_before_test():
	print("##############################")
	action_articles_before(db)

def articles_after_test():
	print("##############################")
	action_articles_after(db)

def test_all():
	# print("Generate users")
	create_user_test()
	# print("\nGenerate articles\n")
	create_article_test()
	# print("\nGenerate comments\n")
	create_comment_test()
	# print("\nGenerate shows\n")
	create_show_test()
	# print("\nGenerate ask\n")
	create_ask_test()
	# print("\nGenerate message\n")
	create_message_test()
	# print("\nGenerate job\n")
	create_job_test()
	# print("\nGenerate vote\n")
	create_vote_test()

	sign_up_test()
	publish_article_test()
	delete_article_test()
	up_vote_test()
	down_vote_test()
	ten_highest_test()
	articles_before_test()
	articles_after_test()


test_all()



