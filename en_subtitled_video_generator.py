import os
import whisper
from moviepy.editor import VideoFileClip
import subprocess

# 設定
input_video_path = "input.mp4"
extracted_audio_path = "audio.wav"
output_srt_path = "subtitles.srt"
output_video_path = "output_with_subs.mp4"

# 削除処理
for path in [extracted_audio_path, output_srt_path, output_video_path]:
    if os.path.exists(path):
        os.remove(path)
        print(f"🧹 削除しました: {path}")

# タイムスタンプのフォーマット変換（Whisperの時間 → SRT形式）
def format_timestamp(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

# ステップ1：mp4 → wav
print("🎞️ MP4 → WAV に変換中...")
video = VideoFileClip(input_video_path)
video.audio.write_audiofile(extracted_audio_path)

# ステップ2：WAV を Whisper で文字起こし
print("🗣 Whisper による英語文字起こし中...")
model = whisper.load_model("base")
result = model.transcribe(extracted_audio_path, task="transcribe")

# ステップ3：SRTファイルとして保存
print("💬 SRT字幕を保存中...")
with open(output_srt_path, "w", encoding="utf-8") as f:
    for i, segment in enumerate(result["segments"]):
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        f.write(f"{i+1}\n")
        f.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
        f.write(f"{text}\n\n")

# ステップ4：ffmpegで字幕を動画に焼き付け
print("📽 字幕を動画に焼き込み中...")
subprocess.run([
    "ffmpeg",
    "-i", input_video_path,
    "-vf", f"subtitles={output_srt_path}:force_style='FontName=NotoSansCJKjp'",
    "-c:a", "copy",
    output_video_path
])

print("✅ 完了！字幕付き動画：", output_video_path)
