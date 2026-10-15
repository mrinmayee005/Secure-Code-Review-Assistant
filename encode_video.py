import subprocess
import imageio_ffmpeg
import os

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

out_video = os.path.join("PCCOE_MrinmayeeKulkarni_124B2B025_CS_AIML", "Video", "demo_video.mp4")

cmd = [
    ffmpeg, "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", "concat_list.txt",
    "-i", "user_voice.wav",
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-r", "30",
    "-c:a", "aac",
    "-b:a", "192k",
    "-t", "326.93",
    out_video
]

print("Running FFmpeg encoding with exact duration 326.93s...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode == 0:
    print("Video encoded successfully! Output:", out_video)
    print("File size:", os.path.getsize(out_video), "bytes")
else:
    print("Error encoding video:")
    print(res.stderr)
