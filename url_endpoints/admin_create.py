from flask import render_template, url_for, redirect
from flask_login import login_required

import database_management.initialise_db_and_lists
from website_management import app
from database_management import db, Track, refresh_tracks_list
from website_forms import AdminEntryContent

@app.route("/admincreate", methods=["GET", "POST"])
@login_required
def admin_create():
    track_object_list = database_management.initialise_db_and_lists.track_object_list
    print(f"admin create tracks value: {track_object_list}")
    admin_create_form = AdminEntryContent()
    if admin_create_form.validate_on_submit():
        print("Submit Valid")
        new_entry = Track(
            title=admin_create_form.title.data,
            artist=admin_create_form.artist.data,
            remix_artist=admin_create_form.remix_artist.data,
            album=admin_create_form.album.data,
            release_date=admin_create_form.release_date.data,
            youtube_url=admin_create_form.youtube_url.data,
            soundcloud_url=admin_create_form.soundcloud_url.data,
            spotify_url=admin_create_form.spotify_url.data,
            description=admin_create_form.description.data,
            img_url=admin_create_form.img_url.data
        )
        db.session.add(new_entry)
        db.session.commit()
        refresh_tracks_list()
        print("refresh taken place")
        print(database_management.initialise_db_and_lists.track_object_list)
        return redirect(url_for('admin_dashboard'))

    return render_template("admineditor.html", form=admin_create_form, is_create=True)