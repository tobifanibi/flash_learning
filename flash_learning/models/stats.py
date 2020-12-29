from flash_learning import db



class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, default=0)
    username = db.Column(db.String(64), index=True, unique=True)

