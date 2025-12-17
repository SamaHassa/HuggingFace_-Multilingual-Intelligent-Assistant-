#وظيفته: توليد محتوى
from transformers import pipeline # استيراد مكتبة التحويلات

def generate_content(topic):
    generator = pipeline("text-generation", model="gpt2")

    result = generator(
        f"Write an informative article about {topic}.",
        max_length=200,
        num_return_sequences=1 #number of sequences to return 
    )

    return result[0]["generated_text"]
