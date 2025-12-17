from content_generation import generate_content
from summarization import summarize_text
from translation import translate_to_french
from question_answering import answer_question

def main():
    topic = "Artificial Intelligence in Healthcare"

    print("Generating content...")
    content = generate_content(topic)
    print("\nGenerated Content:\n", content)

    print("\nSummarizing content...")
    summary = summarize_text(content)
    print("\nSummary:\n", summary)

    print("\nTranslating summary to French...")
    french_translation = translate_to_french(summary)
    print("\nFrench Translation:\n", french_translation)

    print("\nAnswering question...")
    question = "How is artificial intelligence used in healthcare?"
    answer = answer_question(question, content)
    print("\nAnswer:\n", answer)

if __name__ == "__main__":
    main()
