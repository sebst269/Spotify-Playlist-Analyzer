# Spotify Playlist Analyzer

This tool connects to the Spotify API and analyzes a public playlist. It gives you key insights like total duration, top artists, and longest tracks, then exports the data and visualizes it.

## Features

- Connects to Spotify with OAuth
- Pulls playlist title, track count, and full list
- Saves playlist data to `playlist_export.csv`
- Prints summary stats to `playlist_summary.txt`
- Generates a chart of the top 10 longest songs to `top10_longest_tracks`

## Example Output

Exported playlist data to Playlist Info/playlist_export.csv

Saved summary to Playlist Info/playlist_summary.txt

Saved chart to Playlist Info/top10_longest_tracks.png

> Go to spotify-playlist-analyzer/Playlist Info folder to view your playlists' data, summary, and chart

<img width="250" alt="Screen Shot 2025-06-19 at 8 50 24 PM" src="https://github.com/user-attachments/assets/89300b0e-656c-4ba1-8927-b87db6f7c07a" />
<img width="500" alt="Screen Shot 2025-06-19 at 8 51 21 PM" src="https://github.com/user-attachments/assets/82ba9496-ceec-4976-8fcf-50f76e3b7558" />
<img width="250" alt="Screen Shot 2025-06-19 at 8 50 54 PM" src="https://github.com/user-attachments/assets/d3c71892-4d8f-4ce6-838c-831ca9f3d95d" />

## How to Run It

1. Clone the repo

   `git clone https://github.com/sebst269/spotify-playlist-analyzer.git`

   `cd spotify-playlist-analyzer`
   
3. Create a .env file in the root directory with this format:
  
   `SPOTIPY_CLIENT_ID=your_spotify_client_id`

   `SPOTIPY_CLIENT_SECRET=your_spotify_client_secret`

   `SPOTIPY_REDIRECT_URI=http://localhost:8888/callback`
   
> If you're using a tunnel (like `localhost.run`), replace the redirect URI with the one from your tunnel.

> For example: `SPOTIPY_REDIRECT_URI=https://abc123.lhr.life/callback`

4.  If you get stuck on authentication or your browser can’t reach `localhost:8888`, try using a tunnel like localhost.run or ngrok. This can happen in some terminal setups.

5.  Install the dependencies: `pip install -r requirements.txt`

6. Run the script: `python3 src/main.py --summary --export csv --plot`

> You might need to tunnel your localhost using something like [localhost.run](https://localhost.run) if you want the OAuth redirect to work.

## Future Plans

- Maybe turn it into a small web app

## Why I Made This

I wanted to learn how to interact with real APIs, handle OAuth, and analyze live music data in a meaningful way. This was a fun way to build something real-world.

