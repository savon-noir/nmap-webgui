from nmapd import db, config

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(120), unique = True)
    role = db.Column(db.SmallInteger, default = config.ROLE_USER)
    posts = db.relationship('Report', backref = 'owner', lazy = 'dynamic')

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
      return False
    
    def get_id(self):
        return unicode(self.id)

    def credentials_valid(self, password):
        return password == self.password

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    body = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Report %r>' % (self.body)
