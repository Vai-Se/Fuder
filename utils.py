from pytube import YouTube
from json import load


#planning to use this in the future
"""
def check_playlist(url: str) -> bool:
    if "&list=" in url:
        return True
    return False
"""


def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return load(f)


def download_video(url: str, path: str, mode_id: int):
    video = YouTube(url)
    mode = list(MODES.values())[mode_id]
    stream = mode(video.streams)

    print("Downloading video: ", video.title)
    return stream.download(path)


def show_options(options: dict):
    for i, option in enumerate(options.keys()):
        print(f"{i:<5}|{option:>20}")


PATHS = load_json("paths.json")
MODES = {
    "Lowest resolution": lambda streams: streams.get_lowest_resolution(),
    "Highest resolution": lambda streams: streams.get_highest_resolution(),
    "Audio only": lambda streams: streams.get_audio_only()
}
