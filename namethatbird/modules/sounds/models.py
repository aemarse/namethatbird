import datetime
import arrow
from namethatbird.app import db


class XenoCantoSound(db.EmbeddedDocument):
    id = db.IntField(required=True, unique=True)
    genus = db.StringField()
    species = db.StringField()
    subspecies = db.StringField()
    english_name = db.StringField()
    recordist = db.StringField()
    country = db.StringField()
    locality = db.StringField()
    latitude = db.FloatField()
    longitude = db.FloatField()
    sound_type = db.StringField()
    license = db.StringField()
    quality = db.StringField()
    recorded_at = db.DateTimeField()

    def xc_data_to_xc_sound(self, xc_data):
        self.id = int(xc_data.get('id'))
        self.genus = xc_data.get('gen')
        self.species = xc_data.get('sp')
        self.subspecies = xc_data.get('ssp')
        self.english_name = xc_data.get('en')
        self.recordist = xc_data.get('rec')
        self.country = xc_data.get('cnt')
        self.locality = xc_data.get('loc')
        self.latitude = float(xc_data.get('lat'))
        self.longitude = float(xc_data.get('lng'))
        self.sound_type = xc_data.get('type')
        self.license = xc_data.get('lic')
        self.quality = xc_data.get('q')

        timestamp = "%s %s" % (xc_data.get('date'), xc_data.get('time'))
        self.recorded_at = arrow.get(timestamp, 'YYYY-MM-DD HH:mm').datetime


class Sound(db.Document):
    created_at = db.DateTimeField(default=arrow.utcnow().datetime, required=True)
    updated_at = db.DateTimeField(default=arrow.utcnow().datetime, required=True)

    xc_sound = db.EmbeddedDocumentField(XenoCantoSound)
