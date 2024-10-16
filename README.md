---

# Spotify to YouTube MP3 Downloader

This project allows you to automatically download your liked songs from Spotify by searching for them on YouTube and downloading the audio as MP3 files. The downloaded songs are saved to a folder of your choice using `yt-dlp` and FFmpeg for audio extraction.

## Features

- **Spotify Integration**: Fetches your liked songs from Spotify using the Spotify API.
- **YouTube Audio Download**: Searches for each song on YouTube and downloads the highest quality audio available.
- **MP3 Conversion**: Converts the downloaded audio to MP3 format using FFmpeg.
- **Custom Download Folder**: All songs are downloaded and saved in a folder named `Downloaded_Music`.
- **Handles Unicode Characters**: Prints and handles song names that contain special or non-ASCII characters.

## Requirements

To run this project, you need the following dependencies:

1. **Python Packages**  
   Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

   The packages listed in `requirements.txt` are:
   - **Spotipy**: For accessing Spotify’s Web API.
   - **yt-dlp**: A YouTube downloader for extracting and converting audio.
   - **Requests**: For making HTTP requests.
   - **python-dotenv**: For loading environment variables from a `.env` file.

2. **FFmpeg**  
   FFmpeg is required for converting audio files to MP3 format. Follow the instructions below to install it based on your operating system:

   - **macOS**:  
     Install using Homebrew:
     ```bash
     brew install ffmpeg
     ```
   
   - **Linux**:  
     Install using APT (Debian/Ubuntu):
     ```bash
     sudo apt-get install ffmpeg
     ```

   - **Windows**:  
     Download from [FFmpeg.org](https://ffmpeg.org/download.html) and add it to your system's PATH:
     1. Download the Windows build.
     2. Extract the zip folder and place it somewhere on your computer.
     3. Add the `bin` folder of FFmpeg to your system's PATH.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/spotify-to-youtube-downloader.git
   cd spotify-to-youtube-downloader
   ```

2. **Create a `.env` file**:

   Inside the project folder, create a `.env` file and add your Spotify API credentials:

   ```
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=your_redirect_uri
   ```

   You can get these credentials from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).

3. **Install Python dependencies**:

   Run the following command to install all the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**:

   Follow the instructions in the "Requirements" section to install FFmpeg based on your operating system.

## Usage

Once the setup is complete, run the script to download your liked Spotify songs as MP3 files from YouTube:

```bash
python main.py
```

All downloaded MP3 files will be saved to the `Downloaded_Music` folder in the project directory.


## Disclaimer

This project is for educational purposes only. The use of this script to download music may violate the terms of service of Spotify or YouTube, and it's the user's responsibility to ensure they have permission to download and use any content.

---
