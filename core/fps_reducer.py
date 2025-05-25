import subprocess

def reduce_fps(input_path: str, output_path: str, target_fps: int):
    command = [
        'ffmpeg',
        '-i', input_path,
        '-r', str(target_fps),
        '-y',
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"[✔] FPS reduced to {target_fps}. Output saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[✘] FFmpeg failed: {e}")
