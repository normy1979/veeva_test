"""Data models."""
from application import db

class Veevainfo(db.Model):
    rtsm_url = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return '<Veevainfo {}>'.format(self.username)
