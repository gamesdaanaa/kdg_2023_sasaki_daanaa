import moviepy.editor as mp
import speech_recognition as sr
import os

# ffmpegの実行可能ファイルのパスを指定
ffmpeg_path = "/usr/local/bin/ffmpeg"  # ffmpegの実行可能ファイルのパスに適切なものを指定してください

# 環境変数を設定
os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

def extract_audio(video_path, audio_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ja-JP")
    return text

def main():
    video_path = "05文字起こしvideo.mp4"
    audio_path = "05出力結果videos.wav"
    output_text_file = "05出力結果text.txt"

    # 音声抽出
    extract_audio(video_path, audio_path)

    # 音声文字起こし
    transcription = transcribe_audio(audio_path)

    # 結果をテキストファイルに保存
    with open(output_text_file, "w") as file:
        file.write(transcription)

if __name__ == "__main__":
    main()

