from flask import render_template

from website_management import app
from database_management import Track

@app.route("/discography/<int:entry_id>", methods=["GET", "POST"])
def discog_entry(entry_id):
    current_track = Track.query.get(entry_id)
    return render_template("discog_entry.html", track=current_track)