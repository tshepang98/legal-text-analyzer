"""
main.py
Simple legal-text summarizer + named-entity extraction + tone analysis.
Usage:
  python main.py --text "Your legal paragraph here"
  python main.py --file path/to/sample.txt
  python main.py --file path/to/folder_with_txt_files
"""

import argparse
from transformers import pipeline
import spacy
from textblob import TextBlob
from pathlib import Path
import sys

# -------------- Initialize models (lazy load) --------------
print("Initializing models... (this may take a minute the first time)")

try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-6-6")
except Exception as e:
    print("Warning: could not load chosen summarization model, trying default. Error:", e)
    summarizer = pipeline("summarization")

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("spaCy model 'en_core_web_sm' not found. Run: python -m spacy download en_core_web_sm")
    sys.exit(1)

# -------------- Functions --------------
def summarize_text(text, max_length=130, min_length=30):
    words = len(text.strip().split())
    if words < 30:
        return text.strip()
    # dynamically adjust max/min length
    max_len = min(max_length, int(words * 0.7))
    min_len = min(min_length, int(words * 0.3))
    result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return result[0]['summary_text']

def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def analyze_tone(text):
    tb = TextBlob(text)
    return {
        "polarity": round(tb.sentiment.polarity, 3),
        "subjectivity": round(tb.sentiment.subjectivity, 3)
    }

def run_pipeline(text, label=None):
    if label:
        print(f"\n====== Processing: {label} ======\n")
    else:
        print("\n=== ORIGINAL TEXT ===\n")
    print(text.strip())

    print("\n=== SUMMARY ===\n")
    summary = summarize_text(text)
    print(summary)

    print("\n=== NAMED ENTITIES (text, label) ===\n")
    ents = extract_entities(text)
    if ents:
        for e, l in ents:
            print(f"- {e} ({l})")
    else:
        print("No named entities found.")

    print("\n=== TONE / SENTIMENT ===\n")
    print(analyze_tone(text))
    print("\n" + "="*50 + "\n")

# -------------- CLI -------------------------------------------------------hhs
def main():
    parser = argparse.ArgumentParser(description="Legal summarizer + NER + tone")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", type=str, help="Text to summarize")
    group.add_argument("--file", type=str, help="Path to a .txt file or folder with .txt files")
    args = parser.parse_args()

    if args.file:
        p = Path(args.file)
        if not p.exists():
            print("File/folder not found:", args.file)
            return

        # Check if folder
        if p.is_dir():
            for file_path in p.glob("*.txt"):
                text = file_path.read_text(encoding="utf-8")
                run_pipeline(text, label=file_path.name)
        else:
            text = p.read_text(encoding="utf-8")
            run_pipeline(text, label=p.name)
    else:
        run_pipeline(args.text)

if __name__ == "__main__":
    main()
