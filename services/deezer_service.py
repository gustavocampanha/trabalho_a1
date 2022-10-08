import deezer # Importa lip do deezer
import time 
import pandas as pd

## Docs deezer = https://deezer-python.readthedocs.io/en/stable/usage.html

def search_artist(artist):
    deezer_client = deezer.Client()
    print('Conectou ao deezer')
    artist = deezer_client.search_artists(artist)[0] 
    return artist

def search_albuns(artist):
    artist = search_artist(artist)
    print('Artista encontrado, vai detalhar os albuns.')
    return artist.get_albums()

def get_albums_info(artist):
    albums = search_albuns(artist)
    print('Albuns encontrados.')
    artist_data = {
                "album": [], 
                "song": [], 
                "song_position": [], 
                "song_duration": [],
                "song_gaim": [],
                "song_rank": []
                }
    
    albuns_data = {
                "album": [],
                "fans": [],
                "explicit_lyrics": [],
                "duration": []
    }
    
    count_albuns = 0
    for album in albums:
        count_albuns += 1
        print(f'Coletando albuns {count_albuns}/{len(albums)}')
        if album.record_type == "album":
            album_name = album.title
            album_name = album_name.replace("'", "")
            albuns_data["album"].append(album_name)
            albuns_data["duration"].append(album.duration)
            albuns_data["fans"].append(album.fans)
            albuns_data["explicit_lyrics"].append(album.explicit_lyrics)
            songs = album.tracks
            for song in songs:
                song_name = song.title_short
                song_duration = song.duration
                song_position = song.track_position
                song_gain = song.gain
                song_rank = song.rank
                artist_data["album"].append(album_name) 
                artist_data["song"].append(song_name)
                artist_data["song_position"].append(song_position)
                artist_data["song_duration"].append(song_duration)
                artist_data["song_gaim"].append(song_gain)
                artist_data["song_rank"].append(song_rank)
    df_artist = pd.DataFrame.from_dict(artist_data)
    df_albuns = pd.DataFrame.from_dict(albuns_data)
    return df_artist, df_albuns

def info_albuns(artist):
    albums = search_albuns(artist)
