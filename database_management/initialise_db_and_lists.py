from website_management import app
from database_management import db, Track, User

track_object_list = []
user_object_list = []

with app.app_context():
    db.create_all()
    result = db.session.execute(db.select(Track))
    track_object_list = result.scalars().all()
    result = db.session.execute(db.select(User))
    user_object_list = result.scalars().all()

def refresh_tracks_list():
    with app.app_context():
        global track_object_list
        print("pre refresh")
        result1 = db.session.execute(db.select(Track))
        print(f"I am making it this: {db.session.execute(db.select(Track)).scalars().all()}")
        track_object_list = result1.scalars().all()
        print("change should be in effect")
        print(f"the value inside the function is: {track_object_list}")

def refresh_user_list():
    with app.app_context():
        global user_object_list
        result2 = db.session.execute(db.select(User))
        user_object_list = result2.scalars().all()