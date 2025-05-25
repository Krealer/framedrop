from core.fps_reducer import reduce_fps
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Reduce video FPS")
    parser.add_argument("input", help="Path to input video file")
    parser.add_argument("output", help="Path to save the output video")
    parser.add_argument("--fps", type=int, default=15, help="Target FPS (default: 15)")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("Error: Input file does not exist.")
        return

    reduce_fps(args.input, args.output, args.fps)

if __name__ == "__main__":
    main()
