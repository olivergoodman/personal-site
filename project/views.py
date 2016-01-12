from flask import Flask, render_template, request, jsonify, Blueprint
from project import app, db
from project.models import Page

index_page = Page("index", 0)
contact_page = Page("contact", 0)
  
@app.route('/')
@app.route('/index')

def index():
  page_title = 'Oliver Goodman' 
  print 'index was called'
  displayTable()
  return render_template('index.html',
                          title = "Oliver Goodman | Home",
                          page_title = page_title)

@app.route('/contact')
def contact(): 
  displayTable()
  page_title = 'Contact'
  return render_template('contact.html',
							title = 'Oliver Goodman | Contact',
							page_title = page_title)


##example stuff
# def index():
#     user = {'nickname': 'Miguel'}  # fake user
#     posts = [  # fake array of posts
#         { 
#             'author': {'nickname': 'John'}, 
#             'body': 'Beautiful day in Portland!' 
#         },
#         { 
#             'author': {'nickname': 'Susan'}, 
#             'body': 'The Avengers movie was so cool!' 
#         }
#     ]
#     return render_template("index.html",
#                            title='Home',
#                            user=user,
#                            posts=posts)