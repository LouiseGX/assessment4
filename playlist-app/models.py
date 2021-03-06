"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    # ADD THE NECESSARY CODE HERE
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
     
    __tablename__ = 'playlists'
    
    playlist_id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True
                   )
    
    name = db.Column(db.String(50),
                     nullable = False
                     )
    
    description = db.Column(db.Text,
                            nullable = False
                            )
    
    songs = db.relationship('Song',
                            secondary='playlist_songs',
                            backref='playlists')
    
    def __repr__(self):
        return f"<Playlist {self.name}>"
    


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    __tablename__ = 'songs'
    
    song_id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True
                   )
    
    title = db.Column(db.String(50),
                     nullable = False
                     )
    
    artist = db.Column(db.String(75),
                     nullable = False
                     )
    
    def __repr__(self):
        return f"<Song {self.title} - {self.artist}>"
  


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
        
    __tablename__ = 'playlist_songs'
    
    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True
                   )
    
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey('playlists.playlist_id'))
    
    song_id = db.Column(db.Integer,
                        db.ForeignKey('songs.song_id'))
    
   
    
   


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
