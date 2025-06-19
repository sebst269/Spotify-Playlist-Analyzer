# Spotify Playlist Analyzer 🎵

This is a Python script that uses the Spotify API to pull info from a playlist (e.g., names and tracks) and prints it out. I built it to learn how to work with real APIs and handle OAuth authentication.

## Features

- Connects to Spotify with OAuth
- Pulls playlist name, track count, and full track list
- Shows each song and who it’s by
- Uses a `.env` file to keep credentials safe

## Example Output

Playlist name: instrumental jazz

Total tracks: 208

Tracks:

- It Never Entered My Mind by Coleman Hawkins, Ben Webster
- Chloe by Joe Pass
- ...

## How to Run It

1. Clone the repo
2. Create a .env file in the root directory with this format:

  `SPOTIPY_CLIENT_ID=your_spotify_client_id`

  `SPOTIPY_CLIENT_SECRET=your_spotify_client_secret`

  `SPOTIPY_REDIRECT_URI=https://your-url.lhr.life/callback`
  
4. Start a tunnel so Spotify can redirect to your local app:
  
   ❖ Open a new terminal and run: `ssh -R 80:localhost:8888 nokey@localhost.run`
   
   ❖ You’ll get a temporary URL like: `https://39cf1127839f8c.lhr.life`
   
   ❖ Add `/callback` to that and use it in your `.env` file as the redirect URI.
   
3. Install the dependencies:
  
   `pip install -r requirements.txt`

6. Run the script: `python3 src/main.py`

> Note: You might need to tunnel your localhost using something like [localhost.run](https://localhost.run) if you want the OAuth redirect to work.

## Future Plans

- Export data to CSV or JSON
- Visualize the top artists or genres
- Maybe turn it into a small web app later

## Why I Made This

Just wanted to build something cool with music and APIs, and to have a project that works with real-world authentication and data.

