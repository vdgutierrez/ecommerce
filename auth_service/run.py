import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(port=5001)
