⚖️ Legal Text Analyzer
Overview

Legal Text Analyzer is a Python-based prototype designed to assist legal professionals in  d:

Summarizing complex legal documents

Extracting key legal entities

Analyzing tone and sentiment

Its modular pipeline supports rapid review of single paragraphs, files, or entire folders of legal documents.

Features

Text Summarization: Condenses paragraphs into concise summaries using advanced transformer models.

Named Entity Recognition (NER): Identifies organizations, laws, dates, persons, and monetary values.

Tone & Sentiment Analysis: Measures polarity and subjectivity for quick sentiment evaluation.

Batch Processing: Supports both individual files and folders for large-scale document review.

Technical Approach

Summarization: sshleifer/distilbart-cnn-6-6 for a balance of speed and accuracy.

NER: spaCy en_core_web_sm for detecting organizations, laws, dates, and people.

Sentiment Analysis: TextBlob for lightweight polarity and subjectivity analysis.

Architecture: Modular sequential pipeline for easy testing and future upgrades.

CLI User Experience: Flexible input options for text, single files, or batch folders.

Installation

Create a virtual environment and activate it:

python -m venv legal_analyzer
# Linux/macOS
source legal_analyzer/bin/activate
# Windows
legal_analyzer\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Download spaCy language model:

python -m spacy download en_core_web_sm

Usage

Summarize a text string:

python main.py --text "Your legal paragraph here."


Summarize text from a file:

python main.py --file sample.txt


Process all .txt files in a folder:

python main.py --file /path/to/folder_with_txt_files

Example

Input (sample.txt):

This Agreement is made on 20 October 2023 between LexisNexis and ABC Law Firm.
The parties agree to maintain confidentiality in accordance with the Data Protection Act 2018.
The contractor shall provide research services related to case law and statutory interpretation
for a period of twelve months beginning on the date of signing.


Output:

=== SUMMARY ===
This Agreement is made on 20 October 2023 between LexisNexis and ABC Law Firm.
The parties agree to maintain confidentiality in accordance with the Data Protection Act 2018.
The contractor shall provide research services for twelve months.

=== NAMED ENTITIES ===
- 20 October 2023 (DATE)
- LexisNexis (ORG)
- ABC Law Firm (ORG)
- Data Protection Act 2018 (LAW)

=== TONE / SENTIMENT ===
{'polarity': -0.1, 'subjectivity': 0.4}

Libraries & Models

Transformers (Hugging Face): sshleifer/distilbart-cnn-6-6

spaCy: NER with en_core_web_sm

TextBlob: Polarity and subjectivity analysis

PyTorch: Transformer backend

Pathlib: File system handling for batch processing

Limitations & Future Enhancements

Current Limitations:

Optimized for short-to-medium paragraphs; long documents need chunking

General-purpose NER may miss legal-specific entities

AI-generated summaries should be reviewed for accuracy

Initial model loading can be resource-intensive

Future Enhancements:

Legal-specific NER models

Citation extraction & clause classification

Plain-language conversion for non-specialists

User-friendly web interface (Streamlit / FastAPI)

Export results in structured formats (JSON, CSV)

Author

Tshepang Mathlore
