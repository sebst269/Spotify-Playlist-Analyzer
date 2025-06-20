import os
import argparse
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import csv
from collections import Counter
import matplotlib.pyplot as plt

# Load .env
load_dotenv()

# Ensure output folder exists
output_dir = "Playlist Info"
os.makedirs(output_dir, exist_ok=True)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-read-private"
))

# Public playlist URL
playlist_url = "https://open.spotify.com/playlist/6UeSakyzhiEt4NB3UAd6NQ"  # Billboard Hot 100
playlist_id = playlist_url.split("/")[-1].split("?")[0]

# Get playlist data
playlist = sp.playlist(playlist_id)
tracks = playlist["tracks"]["items"]

# Flatten track info
track_list = []
for item in tracks:
    track = item["track"]
    if not track:
        continue
    title = track["name"]
    artists = ", ".join([artist["name"] for artist in track["artists"]])
    duration_s = track["duration_ms"] / 1000  # convert to seconds
    track_list.append({
        "title": title,
        "artists": artists,
        "duration_s": duration_s
    })

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--export", choices=["csv"], help="Export format")
parser.add_argument("--summary", action="store_true", help="Print and save playlist summary")
parser.add_argument("--plot", action="store_true", help="Plot top 10 longest tracks")
args = parser.parse_args()

# Export to CSV
if args.export == "csv":
    csv_path = os.path.join(output_dir, "playlist_export.csv")
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["title", "artists", "duration_s"])
        writer.writeheader()
        for track in track_list:
            writer.writerow(track)
    print(f"Exported playlist data to {csv_path}")

# Summary
if args.summary:
    durations = [t["duration_s"] for t in track_list]
    artists = [artist for track in track_list for artist in track["artists"].split(", ")]

    total_s = sum(durations)
    avg_s = total_s // len(durations)
    top_artists = Counter(artists).most_common(5)
    longest_title = max(track_list, key=lambda t: len(t["title"]))

    summary_lines = [
        f"🎧 Playlist Summary for '{playlist['name']}':",
        f"- Total duration: {int(total_s) // 60} min {int(total_s) % 60} sec",
        f"- Average track length: {int(avg_s) // 60} min {int(avg_s) % 60} sec",
        "- Top 5 most frequent artists:"
    ]
    for artist, count in top_artists:
        summary_lines.append(f"  • {artist} ({count} songs)")
    summary_lines.append(f"- Longest title: \"{longest_title['title']}\" by {longest_title['artists']}")

    summary_path = os.path.join(output_dir, "playlist_summary.txt")
    with open(summary_path, "w") as f:
        for line in summary_lines:
            f.write(line + "\n")
    print(f"Saved summary to {summary_path}")

# Plot
if args.plot:
    top10 = sorted(track_list, key=lambda x: x["duration_s"], reverse=True)[:10]
    titles = [t["title"][:30] + "..." if len(t["title"]) > 30 else t["title"] for t in top10]
    durations = [t["duration_s"] for t in top10]

    plt.figure(figsize=(10, 6))
    plt.barh(titles[::-1], durations[::-1])  # Reverse for top-down view
    plt.xlabel("Duration (seconds)")
    plt.title("Top 10 Longest Tracks in Playlist")
    plt.tight_layout()

    plot_path = os.path.join(output_dir, "top10_longest_tracks.png")
    plt.savefig(plot_path)
    print(f"Saved chart to {plot_path}")
