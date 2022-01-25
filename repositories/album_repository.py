from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

# Create and save album
def save(album):
    sql = "INSERT INTO albums (album_name, genre, album_artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.genre, album.album_artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

# Delete all albums
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

# Find album by ID
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repository.select(result['user_id'])
        album = Album(result['album_name'], result['genre'], artist, result['id'])
    return album

# List all albums
def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['album_name'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

# Edit albums
def update(album):
    sql = "UPDATE albums SET (album_name, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.album_name, album.genre, album.artist.artist_id, album.album_id]
    run_sql(sql, values)

# Delete album
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)