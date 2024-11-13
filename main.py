import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_bootstrap import Bootstrap


class Base(DeclarativeBase):
    pass




db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("APP_CONFIG_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("APP_CONFIG_DATABASE_URI")
bootstrap = Bootstrap(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class AdminLogin(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit1 = SubmitField(label='Log In')

class AdminEntryContent(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    artist = StringField(label='Artist', validators=[DataRequired()])
    remix_artist = StringField(label='Remix Artist')
    album = StringField(label='Album', validators=[DataRequired()])
    release_date = StringField(label='release_date', validators=[DataRequired()])
    youtube_url = StringField(label='YouTube URL', validators=[DataRequired()])
    soundcloud_url = StringField(label='Soundcloud URL', validators=[DataRequired()])
    spotify_url = StringField(label='Spotify URL', validators=[DataRequired()])
    description = TextAreaField(label='Description', validators=[DataRequired()])
    img_url = StringField(label='Image URL', validators=[DataRequired()])
    submit2 = SubmitField(label='Submit')

class AdminEntryID(FlaskForm):
    primary_id = IntegerField(label='id', validators=[DataRequired()])
    submit3 = SubmitField(label='Submit')


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), nullable=False)
    stored_password: Mapped[str] = mapped_column(String(250), nullable=False)

class Track(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    artist: Mapped[str] = mapped_column(String(250), nullable=False)
    remix_artist: Mapped[str] = mapped_column(String(250))
    album: Mapped[str] = mapped_column(String(250), nullable=False)
    release_date: Mapped[str] = mapped_column(String(10), nullable=False)
    youtube_url: Mapped[str] = mapped_column(String(250), nullable=False)
    soundcloud_url: Mapped[str] = mapped_column(String(250), nullable=False)
    spotify_url: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f"<Track {self.title}>"


with app.app_context():
    db.create_all()
    result = db.session.execute(db.select(Track))
    track_object_list = result.scalars().all()


def refresh_tracks_list():
    global track_object_list
    with app.app_context():
        result = db.session.execute(db.select(Track))
        track_object_list = result.scalars().all()




# Creating my salted & hashed password entry for verification of method

# with app.app_context():
#     admin_login = User(username="Admin", stored_password=generate_password_hash("password123",
#                                                                                         method='pbkdf2:sha256',
#                                                                                         salt_length=8))
#     print(f"The username is: {admin_login.username}")
#     print(f"The salted & hashed password is: {admin_login.stored_password}")
#     db.session.add(admin_login)
#     db.session.commit()

# Check the password function:
# with app.app_context():
#     admin_user = db.session.execute(db.select(User).where(User.username == "Admin")).scalar()
#     print(check_password_hash(admin_user.stored_password, "password123"))

my_name = "Plot Twist"


@app.route("/adminlogin", methods=["GET", "POST"])
def admin_login():
    admin_login_form = AdminLogin()
    if admin_login_form.validate_on_submit():
        entered_username = admin_login_form.username.data
        entered_password = admin_login_form.password.data
        user = db.session.execute(db.select(User).where(User.username == entered_username)).scalar()
        if check_password_hash(user.stored_password, entered_password):
            print(f"Checking details...")
            login_user(user)
            print(f"You have been logged in")
            return redirect(url_for('admin_dashboard'))
        else:
            print("Incorrect credentials")
            return redirect(url_for('home_page'))
    return render_template("adminlogin.html", form=admin_login_form)

@app.route("/admindashboard")
@login_required
def admin_dashboard():
    return render_template("admindashboard.html", tracks=track_object_list)

@app.route('/adminamend/<int:entry_id>', methods=["GET", "POST"])
@login_required
def admin_amend(entry_id):
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
    return render_template('adminamend.html', amend_form=admin_amend_form, track=current_entry)

@app.route('/delete/<int:entry_id>')
@login_required
def admin_delete(entry_id):
    track_to_delete = db.get_or_404(Track, entry_id)
    db.session.delete(track_to_delete)
    db.session.commit()
    refresh_tracks_list()
    return redirect(url_for('admin_dashboard'))

@app.route("/admincreate", methods=["GET", "POST"])
@login_required
def admin_create():
    admin_create_form = AdminEntryContent()
    if admin_create_form.validate_on_submit():
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
        return redirect(url_for('admin_dashboard'))

    return render_template("admineditor.html", form=admin_create_form, is_create=True)

@app.route("/")
def home_page():
    return render_template("homepage.html", tracks=track_object_list)

@app.route("/discography")
def discography():
    return render_template("discography.html", tracks=track_object_list)

@app.route("/discography/<int:entry_id>", methods=["GET", "POST"])
def discog_entry(entry_id):
    current_track = Track.query.get(entry_id)
    return render_template("discog_entry.html", track=current_track)

@app.route("/music_production")
def production_page():
    return render_template("production.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/testing")
def testing():
    return render_template("testing.html", tracks=track_object_list)

if __name__ == "__main__":
    app.run(debug=True)