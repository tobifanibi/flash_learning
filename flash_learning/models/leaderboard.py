from sqlalchemy.orm import relationship

from flash_learning import db


class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = relationship("User")
