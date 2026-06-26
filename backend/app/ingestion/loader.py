from pathlib import Path
from pypdf import PdfReader
from docx import Document

import hashlib
import os

def load_pdf(path):
    reader = PdfReader(path)
    texts = []

    for page_no, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            texts.append(f"\n[page={page_no}]\n{text}")

    return "\n".join(texts)

def load_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

def load_txt(path):
    return Path(path).read_text(encoding="utf-8")

def load_file(path: str) -> str:
    suffix = Path(path).suffix.lower()

    if suffix == ".pdf":
        return load_pdf(path)
    if suffix == ".docx":
        return load_docx(path)
    if suffix == ".txt":
        return load_txt(path)

    raise ValueError(f"Unsupported file type: {suffix}")

def compute_md5(filepath):
    """คำนวณ MD5 hash ของไฟล์"""
    md5_hash = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# ทดสอบ: คำนวณ MD5 ของทุกไฟล์
print('📊 MD5 Hash ของแต่ละไฟล์:')
print('=' * 70)
file_hashes = {}
for fname in sorted(os.listdir('data')):
    fpath = f'data/{fname}'
    if os.path.isfile(fpath):
        h = compute_md5(fpath)
        file_hashes[fname] = h
        print(f'  {fname:<25} → {h}')

