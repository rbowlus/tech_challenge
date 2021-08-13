from app import db

class Divvy(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer)
    starttime = db.Column(db.Date)
    stoptime = db.Column(db.Date)
    bikeid = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String)
    usertype = db.Column(db.String)
    gender =  db.Column(db.String)
    birthday = db.Column(db.Date)
    trip_duration = db.Column(db.Integer)

    def __repr__(self):
        pass