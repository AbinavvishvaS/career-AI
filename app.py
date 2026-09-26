from flask import Flask, render_template, request, jsonify

from predict_career import predict_career
from skill_gap import analyze_skill_gap


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data received."
            }), 400

        qualification = data.get("qualification", "")
        interest = data.get("interest", "")
        skills = data.get("skills", [])

        # Validate qualification
        if not qualification:
            return jsonify({
                "error": "Please select your qualification."
            }), 400

        # Validate interest
        if not interest:
            return jsonify({
                "error": "Please select your area of interest."
            }), 400

        # Validate skills
        if not skills:
            return jsonify({
                "error": "Please select at least one technical skill."
            }), 400

        # Predict career
        career = predict_career(
            qualification,
            interest,
            skills
        )

        # Analyze skill gap
        gap = analyze_skill_gap(
            career,
            skills
        )

        # Send result to frontend
        return jsonify({
            "career": career,
            "required_skills": gap["required_skills"],
            "matched_skills": gap["matched_skills"],
            "missing_skills": gap["missing_skills"],
            "skill_gap_percentage": gap["skill_gap_percentage"],
            "learning_recommendations": gap["learning_recommendations"]
        })

    except FileNotFoundError as error:

        return jsonify({
            "error": f"Required file not found: {str(error)}"
        }), 500

    except Exception as error:

        return jsonify({
            "error": f"Prediction error: {str(error)}"
        }), 500


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )