"""Data models."""
from application import db

class Veevainfo(db.Model):
    rtsm_url = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return '<Veevainfo {}>'.format(self.username)

class Subjectinfo(db.Model):
    subject_id = db.Column(db.String, primary_key=True)
    site_number = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String, nullable=False)
    rand_id = db.Column(db.Integer)
    previous_treatment = db.Column(db.Boolean)
    severity = db.Column(db.String)
    cohort = db.Column(db.String)
    randomized_status = db.Column(db.String)
    status_date = db.Column(db.Date)
    next_event = db.Column(db.String)
    
    def __repr__(self):
        return '<Subjectinfo {}>'.format(self.site_number)