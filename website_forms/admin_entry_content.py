from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField

class AdminEntryContent(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    artist = StringField(label='Artist', validators=[DataRequired()])
    remix_artist = StringField(label='Remix Artist')
    album = StringField(label='Album', validators=[DataRequired()])
    release_date = StringField(label='release_date', validators=[DataRequired()])
    youtube_url = StringField(label='YouTube URL')
    soundcloud_url = StringField(label='Soundcloud URL')
    spotify_url = StringField(label='Spotify URL')
    description = TextAreaField(label='Description', validators=[DataRequired()])
    img_url = StringField(label='Image URL', validators=[DataRequired()])
    submit2 = SubmitField(label='Submit')