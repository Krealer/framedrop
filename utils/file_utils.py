import os

def is_valid_video_file(path):
    valid_exts = ('.mp4', '.mov', '.avi', '.mkv', '.webm')
    return os.path.isfile(path) and path.lower().endswith(valid_exts)
