import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp  # Use yt-dlp instead of youtube_dl
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Spotify API credentials
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
SCOPE = "user-library-read"

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE))

# Define the output directory for downloaded music
output_directory = "Downloaded_Music"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Function to get liked songs from Spotify
def get_liked_songs():
    results = sp.current_user_saved_tracks()
    songs = []
    while results:
        for item in results['items']:
            song = item['track']
            songs.append(song['name'] + ' ' + song['artists'][0]['name'])
        if results['next']:
            results = sp.next(results)
        else:
            break
    return songs

# Function to download audio from YouTube using yt-dlp
def download_audio_from_youtube(song_name, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Save to the specified folder
        'noplaylist': True,
        'default_search': 'ytsearch',  # Set the default search to YouTube
        'nooverwrites': True  # Prevent overwriting existing files
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_name])

# Main function
def main():
    liked_songs = get_liked_songs()
    for song in liked_songs:
        try:
            # Print the song name in a way that handles Unicode characters
            print(f"Downloading: {song.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)}")
            download_audio_from_youtube(song, output_directory)  # Pass the output directory
        except Exception as e:
            print(f"Error downloading {song}: {e}")

if __name__ == "__main__":
    main()
