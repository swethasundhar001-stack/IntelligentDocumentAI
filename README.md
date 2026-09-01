# 📄 Intelligent Document AI

An AI-powered document processing system that uses OCR to extract important information from images and PDF documents.

## 🚀 Features

- Upload PNG, JPG, JPEG and PDF documents
- OCR-based text extraction using Tesseract
- Extract important fields automatically
- Name extraction
- Email extraction
- Phone number extraction
- Date extraction
- Amount extraction
- Address extraction
- Download extracted data as JSON
- Simple Streamlit web interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Tesseract OCR
- OpenCV
- Pillow
- Regular Expressions
- PyMuPDF
- JSON

## 📂 Project Structure

```text
IntelligentDocumentAI/
│
├── src/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── nlp/
│   │   └── field_extractor.py
│   │
│   ├── ocr/
│   │   └── ocr_engine.py
│   │
│   ├── preprocessing/
│   │   ├── document_loader.py
│   │   └── image_preprocessing.py
│   │
│   ├── utils/
│   │   └── pipeline.py
│   │
│   └── app.py
│
├── data/
├── models/
├── reports/
├── tests/
├── requirements.txt
└── README.md