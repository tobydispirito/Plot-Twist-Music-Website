from flask import render_template

from website_management import app

@app.route("/music_production")
def production_page():
    return render_template("production.html")