from datetime import datetime

from flash_learning import db


# Create a model for a Flashcard
class Flashcard(db.Model):

    # Add a primary key with a id field
    id = db.Column(db.Integer, primary_key=True)

    # Add a column to the database with the string of the front side of our card
    content_front_side = db.Column(db.String(200), nullable=False)

    # Add a column to the database with the string of the back side of our card
    content_back_side = db.Column(db.String(200), nullable=False)

    # Add date of creation for bookeeping, with a default creation time of whenever it was created
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Add a repprint function just to make it easier to reference this flashcard
    def __repr__(self):
        return '<Flashcard %r>' % self.id
