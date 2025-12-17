# Multilingual Intelligent Assistant for Content Management

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A **multilingual intelligent assistant** built using the Hugging Face library. This project leverages NLP pipelines to **generate, summarize, translate, and answer questions** about content in multiple languages.

---

## 🔹 Features

This project demonstrates the practical use of **four key Hugging Face pipelines**:

| Feature                  | Pipeline                   | Description                                               |
|---------------------------|----------------------------|-----------------------------------------------------------|
| Content Generation        | `text-generation`          | Generates content about a given topic                    |
| Content Summarization     | `summarization`            | Summarizes the generated content for easier understanding|
| Translation               | `translation_en_to_fr`     | Translates the summarized content into French            |
| Question Answering        | `question-answering`       | Answers questions related to the generated content       |

---

## 🔹 API Endpoint

The assistant exposes a **GET endpoint** for retrieving generated and processed content.

**Endpoint:**  

**Request Body (JSON):**
```json
{
  "topic": "Artificial Intelligence in Education",
  "question": "How does AI improve personalized learning?"
}
**Response Body (JSON):**
{
  "topic": "Artificial Intelligence in Education",
  "generated_text": "...",
  "summary": "...",
  "translated_summary_fr": "...",
  "question_answer": {
    "question": "How does AI improve personalized learning?",
    "answer": "..."
  }
}
```

## 🔹 Installation & Requirements

**Clone the repository:**
```bash
git clone https://github.com/SamaHassa/HuggingFace_-Multilingual-Intelligent-Assistant-.git
cd HuggingFace_-Multilingual-Intelligent-Assistant-

pip install -r requirements.txt

python app.py

```
## 🔹 Project Goal

This project was developed as a practical session exercise to demonstrate:

Using Hugging Face pipelines for content generation, summarization, translation, and question answering.

Building a simple API endpoint to interact with NLP models.

Testing API responses with Thunder Client for JSON requests.
