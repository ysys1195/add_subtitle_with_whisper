import whisper
from googletrans import Translator
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

# Whisperモデルの読み込み
print("🗣 Whisperで文字起こし中...")
model = whisper.load_model("base")
result = model.transcribe("audio.wav", task="transcribe")

# 全セグメントを1つの文字列に結合
full_text = " ".join([seg["text"].strip() for seg in result["segments"]])

# 文単位に分割（Punktを直接使用）
punkt_params = PunktParameters()
tokenizer = PunktSentenceTokenizer(punkt_params)
english_sentences = tokenizer.tokenize(full_text)

# 翻訳処理
print("🌐 Google翻訳で文ごとに翻訳中...")
translator = Translator()
output_lines = []

for i, en_text in enumerate(english_sentences, start=1):
    ja_text = translator.translate(en_text, src="en", dest="ja").text
    output_lines.append(f"[{i}]")
    output_lines.append(f"EN: {en_text}")
    output_lines.append(f"JA: {ja_text}")
    output_lines.append("")  # 空行で区切る

# 結果を保存
with open("translated_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("✅ 完了！翻訳結果を保存しました → translated_output.txt")
