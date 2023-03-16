from clipmock import db

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  images = db.relationship('Images', backref='image')

  def __init__(self, username, password):
    self.username = username
    self.password = password

class Images(db.Model):
  id  = db.Column(db.Integer, primary_key=True)
  imagename = db.Column(db.String(100))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __init__(self, imagename, user_id):
    self.imagename = imagename
    self.user_id = user_id
