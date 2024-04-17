from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Pitcher(db.Model, SerializerMixin):
    __tablename__ = "pitcher_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    era = db.Column(db.Float)
    games_started = db.Column(db.Integer)
    innings_pitched = db.Column(db.Float)
    strikeouts = db.Column(db.Integer)
    year = db.Column(db.Integer)

class HockeyEvent(db.Model, SerializerMixin):
    __tablename__ = "hockey_event_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    time = db.Column(db.String(50))
    event = db.Column(db.String(100))
    game_id = db.Column(db.Integer)
    team_name = db.Column(db.String(100))

    def __repr__(self):
        return f'<HockeyEvent {self.name} - {self.event}>'
