import os

from flash_learning import create_app, db

app = create_app()


@app.before_first_request
def create_tables():
    from flash_learning.models.flashcard import Flashcard
    db.create_all()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
