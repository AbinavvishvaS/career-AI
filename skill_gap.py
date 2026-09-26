import json


REQUIREMENTS_PATH = "data/career_requirements.json"


def load_requirements():
    """Load career skill requirements from JSON file."""

    with open(REQUIREMENTS_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def analyze_skill_gap(career, selected_skills):
    """
    Compare student's skills with the skills required
    for the predicted career.
    """

    requirements = load_requirements()

    if career not in requirements:
        raise ValueError(f"Career '{career}' was not found in career_requirements.json")

    required_skills = requirements[career]["required_skills"]

    selected_skills = set(selected_skills)

    matched_skills = [
        skill for skill in required_skills
        if skill in selected_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in selected_skills
    ]

    if len(required_skills) > 0:
        skill_gap_percentage = round(
            (len(missing_skills) / len(required_skills)) * 100,
            2
        )
    else:
        skill_gap_percentage = 0

    learning_recommendations = []

    for skill in missing_skills:

        recommendation = {
            "Python": "Learn Python programming, functions, modules, and object-oriented programming.",
            "Java": "Learn Java programming, OOP concepts, collections, and exception handling.",
            "SQL": "Learn SQL queries, joins, aggregation, and database fundamentals.",
            "HTML": "Learn HTML structure, forms, semantic elements, and web page design.",
            "CSS": "Learn CSS selectors, layouts, Flexbox, Grid, and responsive design.",
            "JavaScript": "Learn JavaScript fundamentals, DOM manipulation, and events.",
            "Pandas": "Learn Pandas for data cleaning, filtering, grouping, and analysis.",
            "NumPy": "Learn NumPy arrays, indexing, mathematical operations, and data processing.",
            "Excel": "Learn Excel formulas, functions, pivot tables, and data analysis.",
            "Data_Visualization": "Learn data visualization using charts, graphs, and visualization libraries.",
            "Machine_Learning": "Learn supervised learning, unsupervised learning, model training, and evaluation.",
            "Scikit_Learn": "Learn Scikit-learn preprocessing, model training, prediction, and evaluation.",
            "Git": "Learn Git basics including repositories, commits, branches, and GitHub.",
            "Linux": "Learn Linux commands, file management, permissions, and shell basics.",
            "Cloud_Computing": "Learn cloud computing fundamentals, virtual machines, storage, and cloud services.",
            "Networking": "Learn networking fundamentals including IP, TCP/IP, DNS, and routing.",
            "Cybersecurity": "Learn cybersecurity fundamentals, threats, authentication, and network security."
        }

        learning_recommendations.append({
            "skill": skill,
            "recommendation": recommendation.get(
                skill,
                f"Learn the fundamentals of {skill}."
            )
        })

    return {
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_gap_percentage": skill_gap_percentage,
        "learning_recommendations": learning_recommendations
    }


if __name__ == "__main__":

    test_career = "ML Engineer"

    test_skills = [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Machine_Learning"
    ]

    result = analyze_skill_gap(
        test_career,
        test_skills
    )

    print("\nRequired Skills:")
    print(result["required_skills"])

    print("\nMatched Skills:")
    print(result["matched_skills"])

    print("\nMissing Skills:")
    print(result["missing_skills"])

    print("\nSkill Gap:")
    print(str(result["skill_gap_percentage"]) + "%")

    print("\nLearning Recommendations:")

    for item in result["learning_recommendations"]:
        print(
            "-",
            item["skill"],
            ":",
            item["recommendation"]
        )