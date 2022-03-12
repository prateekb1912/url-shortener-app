from core import db
from datetime import datetime

class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String(500), nullable = False)
    short_id = db.Column(db.String(20), nullable = False, unique = True)
    created_at = db.Column(db.Datetime(), default = datetime.now(), nullable = False)