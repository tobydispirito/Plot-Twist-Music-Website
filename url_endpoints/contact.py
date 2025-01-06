from flask import render_template

from website_management import app

@app.route("/contact")
def contact():
    return render_template("contact.html")