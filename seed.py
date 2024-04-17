import json
from models import db, Pitcher, HockeyEvent  # Import HockeyEvent as well
from app import app  

if __name__ == "__main__":
    with app.app_context():
        with open("pitchers.json") as f:
            data = json.load(f)
            for pitcher_data in data["pitchers"]:
                pitcher = Pitcher(
                    name=pitcher_data["name"],
                    age=pitcher_data["age"],
                    wins=pitcher_data["wins"],
                    losses=pitcher_data["losses"],
                    era=pitcher_data["era"],
                    games_started=pitcher_data["games_started"],
                    innings_pitched=pitcher_data["innings_pitched"],
                    strikeouts=pitcher_data["strikeouts"],
                    year=pitcher_data["year"]
                )
                db.session.add(pitcher)
            db.session.commit()
            
        with open("hockey_data.json") as f:  
            data = json.load(f)
            for event_data in data:
                event = HockeyEvent(
                    time=event_data["time"],
                    name=event_data["name"],
                    event=event_data["event"],
                    game_id=event_data["game_id"],
                    team_name=event_data["team_name"]
                )
                db.session.add(event)
            db.session.commit()
