from transformers import pipeline

def translate_to_french(text):
    translator = pipeline(
        "translation_en_to_fr",
        model="Helsinki-NLP/opus-mt-en-fr"
    )

    translated = translator(text)
    return translated[0]["translation_text"]
