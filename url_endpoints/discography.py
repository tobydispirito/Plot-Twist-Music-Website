from flask import render_template

from website_management import app
import database_management.initialise_db_and_lists

@app.route("/discography")
def discography():
    track_object_list = database_management.initialise_db_and_lists.track_object_list
    print(f"discography tracks value: {track_object_list}")
    return render_template("discography.html", tracks=track_object_list)