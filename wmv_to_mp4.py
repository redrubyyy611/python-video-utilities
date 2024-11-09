import sys
import moviepy.editor as mpy

if len(sys.argv) < 2 or len(sys.argv) >= 4:
    print("Usage: python wmv_to_mp4.py [-na|--no-audio] <input_file>")
    sys.exit(1)

input_file = sys.argv[1] if len(sys.argv) == 2 else sys.argv[2]
output_file = input_file.replace(".wmv", ".mp4")
should_keep_audio = len(sys.argv) == 3 and sys.argv[1] in ["-na", "--no-audio"]

clip = mpy.VideoFileClip(filename=input_file)
clip.write_videofile(output_file, audio=should_keep_audio)

# clip1 = mpy.VideoFileClip("mp4/scammer-pt1.mp4")
# clip2 = mpy.VideoFileClip("mp4/scammer-pt2.2.mp4")
# final = mpy.concatenate_videoclips([clip1, clip2])
# final.write_videofile("mp4/scammer.mp4", audio=False)
