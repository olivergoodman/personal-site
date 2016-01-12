from flask import Flask, render_template
from project import app, db
from project.models import Page

index_page = Page("index", 0)
contact_page = Page("contact", 0)
  
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
  index_page.visitPage()
  return render_template('contact.html',
							           title = 'Oliver Goodman | Contact',
							           page_title = page_title)

