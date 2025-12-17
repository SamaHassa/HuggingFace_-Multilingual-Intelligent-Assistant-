from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    summary = summarizer(
        text,
        max_length=100,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]
