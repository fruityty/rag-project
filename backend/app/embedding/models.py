# โหลด Embedding Model (ครั้งแรกจะดาวน์โหลดจาก HuggingFace)
from sentence_transformers import SentenceTransformer
import warnings
warnings.filterwarnings('ignore')

try:
    embed_model = SentenceTransformer('intfloat/multilingual-e5-large')
    test = embed_model.encode('ทดสอบ')
    print(f'✅ โหลด Embedding Model สำเร็จ!')
    print(f'   Model: intfloat/multilingual-e5-large')
    print(f'   Vector size: {len(test)}')
except Exception as e:
    print(f'❌ โหลด Model ไม่สำเร็จ: {e}')
    print('💡 ตรวจสอบ: 1) Internet 2) Disk space (ต้องการ ~2GB)')

# ทดสอบ embedding ภาษาไทย
thai_sentences = [
    'query: ปัญญาประดิษฐ์คืออะไร',
    'passage: AI คือสาขาของวิทยาการคอมพิวเตอร์ที่สร้างระบบอัจฉริยะ',
    'passage: Machine Learning เป็นส่วนหนึ่งของ AI ที่เรียนรู้จากข้อมูล',
    'passage: วันนี้อากาศดีมาก ท้องฟ้าแจ่มใส',
    'passage: Vector Database ใช้เก็บข้อมูลแบบเวกเตอร์',
]

# สร้าง embeddings
embeddings = embed_model.encode(thai_sentences)

print(f'📊 สร้าง embedding สำเร็จ!')
print(f'  จำนวนข้อความ: {len(embeddings)}')
print(f'  ขนาด vector: {embeddings.shape[1]} มิติ')
print(f'  ตัวอย่าง vector (5 ค่าแรก): {embeddings[0][:5]}')