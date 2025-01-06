from flask import render_template

from website_management import app

@app.route("/about")
def about():
    return render_template("about.html", title="About")