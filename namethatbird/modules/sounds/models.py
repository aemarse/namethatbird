import datetime
from namethatbird.app import db


class XenoCantoSound(db.EmbeddedDocument):
    id = db.IntField(required=True)
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
    file_url = db.URLField()
    file_license = db.StringField()
    details_url = db.URLField()
    quality = db.StringField()
    recorded_at = db.DateTimeField()


class Sound(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    updated_at = db.DateTimeField(default=datetime.datetime.now, required=True)

    xc_sound = db.EmbeddedDocumentField(XenoCantoSound)
