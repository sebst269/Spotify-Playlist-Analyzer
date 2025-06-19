import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Connect with real user session
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-read-private playlist-read-collaborative"
))

# Public playlist URL
playlist_url = "https://open.spotify.com/playlist/6UeSakyzhiEt4NB3UAd6NQ"  # Billboard Hot 100
playlist_id = playlist_url.split("/")[-1].split("?")[0]

# Fetch playlist
playlist = sp.playlist(playlist_id)
print(f"Playlist name: {playlist['name']}")
print(f"Total tracks: {playlist['tracks']['total']}")
print("Tracks:")
for item in playlist["tracks"]["items"]:
    track = item["track"]
    print(f"- {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")
