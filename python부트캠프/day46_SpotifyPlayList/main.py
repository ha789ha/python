import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = '##'
SECRET = '##'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private"))

## web scrap 100 songs using beautifulsoup
def spotify_list():
        global date
        date = input('몇년도의 노래를 원하나요?(yyyy-mm-dd 형식으로 입력하세요)')
        response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/').text
        soup = BeautifulSoup(response, 'html.parser')
        musics = soup.select(selector='li h3')
        billboard = []

        for i, j in enumerate(musics):
            music = j.getText(strip=True)
            billboard.append(music)
            if i == 99:
                break
        return billboard
# song lists
song_names = spotify_list()

# make songs url
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# make playlists
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# add songs in  playlists
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# final playlists
print(playlist)