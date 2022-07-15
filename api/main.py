from constants import API_PORT, MONGO_PORT
from init import create_app
from pymongo import MongoClient

client = MongoClient('localhost', MONGO_PORT)
db = client.flask_db
todos = db.todos

app = create_app()
if __name__ == "__main__":
    app.run(port=API_PORT)
    app.debug = True
