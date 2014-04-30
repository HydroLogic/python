import sqlite3


class Album:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.tracks = []

class Track:
    def __init__(self, bytes, composer, id, milliseconds, name, unit_price):
        self.bytes = bytes
        self.composer = composer
        self.id = id
        self.milliseconds = milliseconds
        self.name = name
        self.unit_price = unit_price


albums_by_id = {}
conn = sqlite3.connect('chinook.sqlite')
try:
    cur = conn.cursor()
    try:
        for row in cur.execute('SELECT AlbumId, Title FROM Album'):
            album = Album(row[0], row[1])
            albums_by_id[album.id] = album

        for row in cur.execute('SELECT AlbumId, Bytes, Composer, TrackId, Milliseconds, Name, UnitPrice FROM Track'):
            album_id = row[0]
            track = \
                Track(
                    bytes=row[1],
                    composer=row[2],
                    id=row[3],
                    milliseconds=row[4],
                    name=row[5],
                    unit_price=row[6]
                )
            album = albums_by_id[album_id]
            album.tracks.append(track)
    finally:
        cur.close()
finally:
    conn.close()

for album in albums_by_id.itervalues():
    for track in album.tracks:
        print album.title, '***', track.name
    print
