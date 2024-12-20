# Mashup Generator

The Mashup Generator is a Python script that generates a mashup of songs by downloading audio files from YouTube, trimming them to a specified duration, merging them, and converting the output into an MP3 format.


## Author

- **[Guryansh](https://github.com/Guryansh)**

---

## Features

- **Customizable Inputs**: Specify the artist's name, the number of songs, and the duration of each audio clip.
- **Automated Workflow**: Downloads audio from YouTube, converts formats, trims, and merges audio files.
- **API Integration**: Uses external APIs for audio format conversion.
- **Cross-Platform Support**: Works on any platform with Python installed.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Guryansh/Mashup
   ```
2. Navigate to the project directory:
   ```bash
   cd mashup-generator
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

To generate a mashup, use the following command:

```bash
python 102218044.py <SingerName> <NumberOfVideos> <AudioDuration> <resultFileName>
```

### Parameters:
- `<SingerName>`: Name of the artist or band.
- `<NumberOfVideos>`: Number of YouTube videos to include.
- `<AudioDuration>`: Duration (in seconds) for each audio clip.
- `<resultFileName>`: Name of the output MP3 file.

### Example:
```bash
python 102218044.py "Taylor Swift" 5 30 "mashup.mp3"
```

---

## Process Flow

1. Search for the specified number of songs by the artist on YouTube.
2. Download the audio of the songs in `.webm` format.
3. Convert `.webm` files to `.wav`.
4. Trim audio files to the specified duration.
5. Merge trimmed audio files into a single `.wav` file.
6. Convert the final `.wav` file to `.mp3`.

![image](https://github.com/user-attachments/assets/562c79f2-16ba-4222-bdbb-f852b8ab4d8b)

---

## Dependencies

- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: For downloading YouTube videos.
- **[moviepy](https://pypi.org/project/moviepy/)**: For audio processing.
- **[youtubesearchpython](https://pypi.org/project/youtubesearchpython/)**: For searching videos on YouTube.
- **[requests](https://pypi.org/project/requests/)**: For API integration.

---

## Live Link

Check out the live version of the app: [Mashup Generator](https://mashup-six.vercel.app)

---
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
