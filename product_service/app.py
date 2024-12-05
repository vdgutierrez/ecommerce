from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Configuración de MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["product_catalog"]

from routes import *

if __name__ == "__main__":
    app.run(port=5001, debug=True)
