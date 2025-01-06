from flask import render_template

from website_management import app
import database_management.initialise_db_and_lists

@app.route("/")
def home_page():
    track_object_list = database_management.initialise_db_and_lists.track_object_list
    print("All OK here")
    return render_template("homepage.html", tracks=track_object_list)