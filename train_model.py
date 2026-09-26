import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


DATA_PATH = "data/careerpilot_dataset.csv"
MODEL_PATH = "models/career_model.pkl"


FEATURE_COLUMNS = [
    "Qualification",
    "Interest",
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

TARGET_COLUMN = "Career"


def main():

    print("=" * 60)
    print("CareerPilot AI - Model Training")
    print("=" * 60)

    # ----------------------------------------
    # 1. Load dataset
    # ----------------------------------------

    print("\nLoading dataset...")

    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)

    # ----------------------------------------
    # 2. Check missing values
    # ----------------------------------------

    print("\nChecking missing values...")

    print(df.isnull().sum().sum(), "missing values found.")

    # ----------------------------------------
    # 3. Prepare X and y
    # ----------------------------------------

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    print("\nInput features:", len(FEATURE_COLUMNS))
    print("Target column:", TARGET_COLUMN)

    # ----------------------------------------
    # 4. Train/test split
    # ----------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nTraining records:", len(X_train))
    print("Testing records:", len(X_test))

    # ----------------------------------------
    # 5. Separate categorical and numeric
    # ----------------------------------------

    categorical_features = [
        "Qualification",
        "Interest"
    ]

    numeric_features = [
        column
        for column in FEATURE_COLUMNS
        if column not in categorical_features
    ]

    # ----------------------------------------
    # 6. Preprocessing
    # ----------------------------------------

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            ),
            (
                "numeric",
                "passthrough",
                numeric_features
            )
        ]
    )

    # ----------------------------------------
    # 7. Random Forest
    # ----------------------------------------

    classifier = RandomForestClassifier(
        n_estimators=50,
        max_depth=12,
        min_samples_leaf=2,
        max_features="sqrt",
        random_state=42,
        n_jobs=-1
    )

    # ----------------------------------------
    # 8. Complete pipeline
    # ----------------------------------------

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", classifier)
        ]
    )

    # ----------------------------------------
    # 9. Train
    # ----------------------------------------

    print("\nTraining Random Forest...")

    model.fit(X_train, y_train)

    print("Training completed.")

    # ----------------------------------------
    # 10. Prediction
    # ----------------------------------------

    predictions = model.predict(X_test)

    # ----------------------------------------
    # 11. Evaluation
    # ----------------------------------------

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)

    print(
        f"\nTest Accuracy: "
        f"{accuracy:.4f} "
        f"({accuracy * 100:.2f}%)"
    )

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions
        )
    )

    # ----------------------------------------
    # 12. Save model
    # ----------------------------------------

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH,
        compress=3
    )

    model_size = (
        os.path.getsize(MODEL_PATH)
        / (1024 * 1024)
    )

    print("=" * 60)
    print("MODEL SAVED")
    print("=" * 60)

    print("\nLocation:")
    print(MODEL_PATH)

    print(
        f"\nModel size: "
        f"{model_size:.2f} MB"
    )

    if model_size <= 10:
        print("Model is below 10 MB.")
    else:
        print("Warning: Model is larger than 10 MB.")


if __name__ == "__main__":
    main()