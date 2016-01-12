from flask import Flask, render_template
from project import app, db
from project.models import Page

#initializing 2 Page objects, index and contact
index_page = Page("index")
contact_page = Page("contact")
  
@app.route('/')
@app.route('/index')
def index():
  page_title = 'Oliver Goodman' 
  print 'index was called'
  index_page.visitPage()
  return render_template('index.html',
                          title = "Oliver Goodman | Home",
                          page_title = page_title)

@app.route('/contact')
def contact(): 
  page_title = 'Contact'
  contact_page.visitPage()
  return render_template('contact.html',
							           title = 'Oliver Goodman | Contact',
							           page_title = page_title)

