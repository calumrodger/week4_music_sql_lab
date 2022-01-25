import pdb
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("Jeff Mills")
artist_repository.save(artist_1)
album_2 = Album("Exhibitionist", "techno", "Jeff Mills")
album_repository.save(album_2)
artist_2 = Artist("Richie Hawtin")
artist_repository.save(artist_2)
album_2 = Album("Decks FX and 909", "techno", "Richie Hawtin")
album_repository.save(album_2)
album_3 = Album("Closer to the Edit", "minimal techno", "Richie Hawtin")
album_repository.save(album_3)
artist_3 = Artist("Akufen")
artist_repository.save(artist_3)
album_4 = Album("My Way", "glitch house", "Akufen")
album_repository.save(album_4)