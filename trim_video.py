# Usage: python trim_video.py <input_file> <start_time> <end_time> <output_file>
# Example: python trim_video.py video.mp4 0 5 trimmed_video.mp4

import sys
import moviepy.editor as mpy

if len(sys.argv) != 5:
    print("Usage: python trim_video.py <input_file> <start_time> <end_time> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
start_time = sys.argv[2]
end_time = sys.argv[3]
output_file = sys.argv[4]

try:
    clip:mpy.VideoFileClip = mpy.VideoFileClip(filename=input_file).subclip(start_time, end_time)
    clip.write_videofile(output_file)
except Exception as e:
    print(f"An error occurred and trimming the video failed: {e}")
    sys.exit(1)

print(f"Video successfully trimmed and saved as {output_file}.")
