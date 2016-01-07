from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)

# Configure the database
app.config['MONGODB_SETTINGS'] = {
    'db': 'namethatbird',
    'host': 'localhost',
    'port': 10036
}

db = MongoEngine(app)

# Import and register the application views
from namethatbird.modules.home.views import HomeView
HomeView.register(app)


if __name__ == '__main__':
    app.run(debug=True)