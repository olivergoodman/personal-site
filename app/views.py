from flask import Flask, render_template
from app import app
import sqlite3

#---------------------DB-------------------------
conn = sqlite3.connect('page_hits.db')
print "Opened database successfully";

# #creating table
# conn.execute('''CREATE TABLE PAGEHITS
#        (NAME  TEXT  NOT NULL,
#        HITS   INT PRIMARY KEY   NOT NULL);''')
# print "Table created successfully";

#adding entries
# conn.execute("INSERT INTO PAGEHITS (NAME, HITS) \
#       VALUES ('Home', 0)");

# conn.execute("INSERT INTO PAGEHITS (NAME, HITS) \
#       VALUES ('Contact', 0)");

# conn.commit()
# print "Records created successfully";

#displaying
def displayTable():
  cursor = conn.execute("SELECT name, hits  from PAGEHITS")
  for row in cursor:
    print "NAME = ", row[0]
    print "HITS = ", row[1], "\n"

def incrementHomeHits():
  conn.execute("UPDATE PAGEHITS SET HITS = HITS + 1 WHERE NAME = Home")

def incrementContactHits():
  conn.execute("UPDATE PAGEHITS SET HITS = HITS + 1 WHERE NAME = Contact")

#----------------------------------------------
  
@app.route('/')
@app.route('/index')

def index():
  page_title = 'Oliver Goodman' 
  title = 'Home'
  print 'index was called'
  incrementHomeHits()
  displayTable()
  return render_template('index.html',
                          title = title,
                          page_title = page_title)

@app.route('/contact')
def contact(): 
  incrementContactHits()
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