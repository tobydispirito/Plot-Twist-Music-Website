from flask import render_template, url_for, redirect
from flask_login import login_required

import database_management.initialise_db_and_lists
from website_management import app
from database_management import db, Track, refresh_tracks_list
from website_forms import AdminEntryContent

@app.route('/adminamend/<int:entry_id>', methods=["GET", "POST"])
@login_required
def admin_amend(entry_id):
    track_object_list = database_management.initialise_db_and_lists.track_object_list
    print(f"admin amend tracks value: {track_object_list}")
    current_entry = db.get_or_404(Track, entry_id)
    admin_amend_form = AdminEntryContent(
        title=current_entry.title,
        artist=current_entry.artist,
        remix_artist=current_entry.remix_artist,
        album=current_entry.album,
        release_date=current_entry.release_date,
        youtube_url=current_entry.youtube_url,
        soundcloud_url=current_entry.soundcloud_url,
        spotify_url=current_entry.spotify_url,
        description=current_entry.description,
        img_url=current_entry.img_url
    )
    if admin_amend_form.validate_on_submit():
        current_entry.title = admin_amend_form.title.data
        current_entry.artist = admin_amend_form.artist.data
        current_entry.remix_artist = admin_amend_form.remix_artist.data
        current_entry.album = admin_amend_form.album.data
        current_entry.release_date = admin_amend_form.release_date.data
        current_entry.youtube_url = admin_amend_form.youtube_url.data
        current_entry.soundcloud_url = admin_amend_form.soundcloud_url.data
        current_entry.spotify_url = admin_amend_form.spotify_url.data
        current_entry.description = admin_amend_form.description.data
        current_entry.img_url = admin_amend_form.img_url.data
        db.session.commit()
        refresh_tracks_list()
        return redirect(url_for('admin_dashboard'))
    return render_template('adminamend.html', amend_form=admin_amend_form, track=current_entry, title="Amend Entry")