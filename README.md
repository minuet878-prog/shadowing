# English Shadowing Practice Tool

A terminal-based English shadowing practice tool built as the final project for CS50P. Tired of constantly scrolling back and forth on YouTube just to follow along with subtitles, I built this tool to automatically extract subtitles from any YouTube video and present them sentence by sentence for a smoother shadowing experience.

## Features

- Downloads subtitles from any YouTube video using yt-dlp — just copy and paste the URL directly from your browser.
- Automatically parses the downloaded subtitle file and removes timestamps, leaving only the clean text.
- Presents subtitles sentence by sentence, letting you practice at your own pace by pressing Enter to continue.
- Exports a clean transcript as a .txt file after the practice session.

## Installation

1.Clone the repository:
```bash
git clone https://github.com/minuet878-prog/shadowing.git
cd shadowing
```

2.Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the program from your terminal:
```bash
python project.py
```
You will be prompted to enter a Youtube URL. Paste the URL of the video you want to practice with, and the program will handle the rest.

Once the subtitles are ready, they will be presented one sentence at a time.Press **Enter** to move to the next sentence. When you are done,press **q** and then **Enter** to quit.

After the session, a .txt transcript of the sentences you practiced will be saved automatically.

## File Structure
```
shadowing/
├── project.py      # Main entry point
├── downloader.py   # Handles subtitle downloading via yt-dlp
├── parser.py       # Parses the .vtt subtitle file into structured data
├── practice.py     # Manages the interactive practice session
├── test_project.py # Unit tests
└── requirements.txt
```