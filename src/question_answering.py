from transformers import pipeline

def answer_question(question, context):
    qa = pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad"
    )

    answer = qa(
        question=question,
        context=context
    )

    return answer["answer"]
