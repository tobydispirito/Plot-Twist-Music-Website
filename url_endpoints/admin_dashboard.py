from flask import render_template
from flask_login import login_required

import database_management.initialise_db_and_lists
from website_management import app

@app.route("/admindashboard")
@login_required
def admin_dashboard():
    track_object_list = database_management.initialise_db_and_lists.track_object_list
    print(f"admin dashboard tracks value: {track_object_list}")
    return render_template("admindashboard.html", tracks=track_object_list)