# TranslateMovie

英語の動画を字幕付きに変換するツール

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
pip install moviepy==1.0.3 openai-whisper ffmpeg-python googletrans==4.0.0-rc1 nltk

# punkt モデルのダウンロード（初回のみ必要）
python -c "import nltk; nltk.download('punkt')"

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
2. 以下のコマンドのいずれかを実行

```bash
# 英語音声に英語字幕をつける（Whisperのみ使用）
python en_subtitled_video_generator.py

# 英語音声を日本語字幕付きに変換する（Whisper + Google翻訳）
python jp_subtitled_video_generator.py

# 英語と日本語の対訳テキストファイルを生成する（文単位で翻訳）
python translate_to_jp.py
```

3. 処理が完了すると output_with_subs.mp4 や translated_output.txt が生成されます

## ファイルの説明

- en_subtitled_video_generator.py: Whisperで英語音声を文字起こしし、英語字幕付き動画を出力
- jp_subtitled_video_generator.py: Whisperで文字起こし後、Google翻訳で日本語に翻訳し、日本語字幕を付与
- translate_to_jp.py: 英語音声を文字起こしし、文ごとに日本語翻訳して英日対訳ファイルを出力（自然な文単位で処理）
- input.mp4: 処理対象の動画ファイル
- output_with_subs.mp4: 字幕付きの出力動画
- translated_output.txt: 英語と日本語の文ごとの対訳ファイル
