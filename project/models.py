from project import db

class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	page_hits = db.Column(db.Integer)

	def __init__(self, name, page_hits):
		name = self.name
		page_hits = self.page_hits

	def __repr__(self):
		return '<Page %d>' % self.id