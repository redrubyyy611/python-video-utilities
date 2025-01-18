import sys
import moviepy.editor as mpy

if len(sys.argv) < 2 or len(sys.argv) >= 4:
    print("Usage: python wmv_to_mp4.py [-na|--no-audio] <input_file>")
    sys.exit(1)

input_file = sys.argv[1] if len(sys.argv) == 2 else sys.argv[2]
current_file_extension = input_file.split(".")[-1]

if current_file_extension == "mp4":
    print("The input file is already an mp4 file.")
    sys.exit(0)

output_file = input_file.replace(f".{current_file_extension}", ".mp4")
should_keep_audio = len(sys.argv) == 3 and sys.argv[1] in ["-na", "--no-audio"]

try:
    clip = mpy.VideoFileClip(filename=input_file)
    clip.write_videofile(output_file, audio=should_keep_audio)
except Exception as e:
    print(f"An error occurred and conversion to MP4 failed: {e}")
    sys.exit(2)
