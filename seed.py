import json
from models import db, Pitcher  
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

                # Add Pitcher object to the session and commit changes
                db.session.add(pitcher)

            db.session.commit()
