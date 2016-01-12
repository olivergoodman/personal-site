from project import db

class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	page_hits = db.Column(db.Integer)

	def __init__(self, name): #initalize new page to 0 page_hits
		name = self.name
		page_hits = 0

	def __repr__(self):
		return '<Page %d>' % self.name

	def visitPage(self):
		self.page_hits = self.page_hits + 1 #incrememnting page by 1 on visit --- ? 