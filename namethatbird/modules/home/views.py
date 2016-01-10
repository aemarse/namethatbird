from flask import render_template, json, jsonify
from flask.ext.classy import FlaskView


class HomeView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('index.html')

    def random(self):
        from namethatbird.modules.sounds.models import Sound

        # Get random recording from database
        rand_rec = Sound.get_random_recording()

        # Format and return json response
        return jsonify(**rand_rec.as_dict())
