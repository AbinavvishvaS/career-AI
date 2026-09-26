import joblib
import pandas as pd


MODEL_PATH = "models/career_model.pkl"

# Load trained model
model = joblib.load(MODEL_PATH)


# Same skill columns used during training
SKILLS = [
    "Python",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Pandas",
    "NumPy",
    "Excel",
    "Data_Visualization",
    "Machine_Learning",
    "Scikit_Learn",
    "Git",
    "Linux",
    "Cloud_Computing",
    "Networking",
    "Cybersecurity"
]


def predict_career(qualification, interest, selected_skills):
    """
    Predict a career based on qualification, interest,
    and selected technical skills.
    """

    # Create one input row
    input_data = {
        "Qualification": qualification,
        "Interest": interest
    }

    # Convert selected skills into 0/1 values
    for skill in SKILLS:
        if skill in selected_skills:
            input_data[skill] = 1
        else:
            input_data[skill] = 0

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict career
    prediction = model.predict(input_df)

    return prediction[0]


# Test when this file is run directly
if __name__ == "__main__":

    test_qualification = "B.E"
    test_interest = "AI"

    test_skills = [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Machine_Learning",
        "Scikit_Learn",
        "Git"
    ]

    career = predict_career(
        test_qualification,
        test_interest,
        test_skills
    )

    print("Predicted Career:", career)