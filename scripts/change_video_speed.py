# Description: This script changes the speed of a video file.
#
# Usage: python change_video_speed.py <input_file> <speed>
# Example: python change_video_speed.py video.mp4 0.25

from moviepy.editor import VideoFileClip
from moviepy.video.fx.speedx import speedx
import sys

if len(sys.argv) != 3:
    print("Usage: python change_video_speed.py <input_file> <speed>")
    sys.exit(1)

input_file = sys.argv[1]

if not input_file.endswith(".mp4"):
    print("The input file should be an mp4 file.")
    sys.exit(1)

try:
    desired_speed_factor = float(sys.argv[2])
except ValueError:
    print("The speed factor should be a number.")
    sys.exit(2)

clip = VideoFileClip(input_file)
output_file = input_file.replace(".mp4", f"-{desired_speed_factor}x.mp4")
edit:VideoFileClip = clip.fx(speedx, desired_speed_factor)
edit.write_videofile(output_file)

print(f"Video speed successfully changed to {desired_speed_factor}x and saved as {output_file}.")
