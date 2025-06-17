import os
from core.fps_reducer import reduce_fps
from utils.file_utils import is_valid_video_file

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'
TARGET_FPS = 10

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

input_files = [f for f in os.listdir(INPUT_DIR)
               if is_valid_video_file(os.path.join(INPUT_DIR, f))]

if not input_files:
    print("No valid video files found in 'input/' folder.")
else:
    for filename in input_files:
        input_path = os.path.join(INPUT_DIR, filename)
        name, _ = os.path.splitext(filename)
        output_filename = f"{name}_10fps.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        print(f"Processing: {filename} -> {output_filename}")
        reduce_fps(input_path, output_path, TARGET_FPS)

