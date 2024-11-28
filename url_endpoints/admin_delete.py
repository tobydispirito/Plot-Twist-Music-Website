from flask import url_for, redirect
from flask_login import login_required

from website_management import app
from database_management import db, Track, refresh_tracks_list

@app.route('/delete/<int:entry_id>')
@login_required
def admin_delete(entry_id):
    track_to_delete = db.get_or_404(Track, entry_id)
    db.session.delete(track_to_delete)
    db.session.commit()
    refresh_tracks_list()
    return redirect(url_for('admin_dashboard'))