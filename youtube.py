#!/usr/bin/env python

from pyperclip import paste
from utils import *
import click


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("url", type=str, required=False)
@click.option("-m", "--mode", type=int, required=False,
              help="Format or quality to download")
@click.option("-o", "--path", type=str, required=False, help="Output path")

def main(url, mode, path):
    """Download YouTube videos easily"""
    if not url:
        url = input("Enter url [Empty=from clipboard]: ") or paste()
    print("Url:", url)

    if not mode:
        print("\nModes:")
        show_options(MODES)

        mode = int(input(f"Choose mode [{DEFAULT['MODE']}]: ")
                   or DEFAULT["MODE"])
    print("Mode:", list(MODES.keys())[mode])

    if not path:
        print("\nPaths:")
        show_options(PATHS)

        path_id = int(input(f"Choose path [{DEFAULT['PATH']}]: ")
                      or DEFAULT['PATH'])
        if path_id == 0:
            path = input("Enter custom path: ")
        else:
            path = list(PATHS.values())[path_id]
    print("Path:", path)

    print("\nDownloading...")
    print("\nUrl:", url)
    print("Mode:", list(MODES.keys())[mode])
    print("Path:", path, "\n")

    try:
        download_video(url, path, mode)
    except Exception as e:
        print("Error while downloading: ", e)
    else:
        print("Done!")


if __name__ == "__main__":
    timer = exec_time(main)
    print(f"Execution time: {timer:.2f}s")
    input("Press enter to exit...")
