---

# 🎵 Spotify to YouTube Audio Downloader

This project is a Python-based tool that allows users to download MP3 audio tracks of their liked songs on Spotify by searching for corresponding tracks on YouTube using `yt-dlp`. The downloaded songs are automatically saved in a specified folder, making it simple to listen to your favorite music offline.

## 🌟 Features
- **Spotify Integration**: Fetches liked songs from your Spotify account.
- **YouTube Search & Download**: Automatically searches for the corresponding song on YouTube and downloads the audio.
- **MP3 Conversion**: Uses `yt-dlp` and `ffmpeg` to convert YouTube audio into high-quality MP3 files.
- **Folder Management**: All downloaded songs are saved into a user-defined folder.
  
## ⚙️ Setup & Usage

### 1. Prerequisites
- Python 3.8+
- Spotify API credentials (Client ID, Client Secret)
- YouTube Data API
- `ffmpeg` installed
- `yt-dlp` and `spotipy` Python libraries

### 2. Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spotify-to-youtube-downloader.git
   cd spotify-to-youtube-downloader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file with your **Spotify** and **YouTube API** credentials:
     ```bash
     SPOTIPY_CLIENT_ID=your_spotify_client_id
     SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
     SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
     ```

### 3. Running the Script
1. Run the script to start downloading your liked songs:
   ```bash
   python main.py
   ```

   The MP3 files will be saved in the `Downloaded_Music` folder.
