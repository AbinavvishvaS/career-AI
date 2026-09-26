import pandas as pd


DATA_PATH = "data/careerpilot_dataset.csv"


df = pd.read_csv(DATA_PATH)


print("=" * 50)
print("CareerPilot AI Dataset Analysis")
print("=" * 50)


print("\nDataset shape:")
print(df.shape)


print("\nColumns:")
for column in df.columns:
    print("-", column)


print("\nMissing values:")
print(df.isnull().sum())


print("\nDuplicate rows:")
print(df.duplicated().sum())


print("\nCareer distribution:")
print(df["Career"].value_counts())


print("\nFirst five records:")
print(df.head())