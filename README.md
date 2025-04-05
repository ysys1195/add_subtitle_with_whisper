# TranslateMovie

英語の動画を日本語字幕付きに変換するツール

## セットアップ方法

### 仮想環境の作成

```bash
# 仮想環境を作成
python -m venv venv

# 仮想環境を有効化
# Windowsの場合
venv\Scripts\activate
# macOS/Linuxの場合
source venv/bin/activate
```

### 必要なパッケージのインストール

```bash
# 必要なパッケージをインストール
pip install moviepy==1.0.3 openai-whisper ffmpeg-python

# ffmpegのインストール
# macOSの場合
brew install ffmpeg
# Ubuntuの場合
# sudo apt update && sudo apt install ffmpeg
# Windowsの場合
# https://ffmpeg.org/download.html からダウンロードしてパスを通す
```

## 使用方法

1. `input.mp4` という名前で変換したい動画ファイルを配置
2. 以下のコマンドを実行

```bash
python subtitled_video_generator.py
```

3. 処理が完了すると `output_with_subs.mp4` が生成されます
