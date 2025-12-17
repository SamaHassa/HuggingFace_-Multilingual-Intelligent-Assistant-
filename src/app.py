# Import Flask to build REST API
from flask import Flask, request, jsonify

# Import our NLP functions from Part 1
from content_generation import generate_content
from summarization import summarize_text
from translation import translate_to_french
from question_answering import answer_question

# Create Flask application
app = Flask(__name__)

# This endpoint handles AI assistant requests
@app.route("/docs", methods=["POST"])
def ai_assistant():

    # Read JSON data sent by the user
    data = request.get_json()

    # Extract topic and question from request
    topic = data["topic"]
    question = data["question"]

    # Run AI pipelines
    generated_text = generate_content(topic)
    summary = summarize_text(generated_text)
    translated_summary_fr = translate_to_french(summary)
    answer = answer_question(question, generated_text)

    # Build response JSON
    response = {
        "topic": topic,
        "generated_text": generated_text,
        "summary": summary,
        "translated_summary_fr": translated_summary_fr,
        "question_answer": {
            "question": question,
            "answer": answer
        }
    }

    # Return JSON response to the client
    return jsonify(response)


# Run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
