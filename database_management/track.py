from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from database_management.db_manager import db

class Track(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    artist: Mapped[str] = mapped_column(String(250), nullable=False)
    remix_artist: Mapped[str] = mapped_column(String(250))
    album: Mapped[str] = mapped_column(String(250), nullable=False)
    release_date: Mapped[str] = mapped_column(String(10), nullable=False)
    youtube_url: Mapped[str] = mapped_column(String(250))
    soundcloud_url: Mapped[str] = mapped_column(String(250))
    spotify_url: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f"<Track {self.title}>"