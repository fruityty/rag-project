
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re

def fixed_size_chunk(text, chunk_size=200, overlap=50):
    """ตัดข้อความตามจำนวนตัวอักษรที่กำหนด"""
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap  # เลื่อนกลับมาซ้อนเพื่อไม่ให้ขาดบริบท

    return chunks

def recursive_char_chunk(text, chunk_size=200, overlap=50, separators=['\n\n', '\n', '。', r'\. ', ' ', '']):
    # Recursive Character Chunking
    # ตัดข้อความตาม separator
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=separators,  # ลำดับการแบ่ง
    )
    recursive_chunks = recursive_splitter.split_text(text)
    return recursive_chunks

def sentence_chunk(text, max_sentences=3):
    """ตัดข้อความตามประโยค/บรรทัด (เหมาะกับภาษาไทย)"""
    # ภาษาไทยใช้ newline เป็นตัวแบ่งประโยคหลัก
    sentences = re.split(r'\n+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    chunks = []
    for i in range(0, len(sentences), max_sentences):
        chunk = '\n'.join(sentences[i:i+max_sentences])
        if chunk:
            chunks.append(chunk)
    return chunks
