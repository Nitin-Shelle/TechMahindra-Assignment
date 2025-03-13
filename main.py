import pandas as pd
import json

# File paths
csv_file = r"D:\Python\Pandas\Assignment\test_input_DataSet1.csv"
json_file = r"D:\Python\Pandas\Assignment\test_input_Dataset2.json"
test_output_file = r"D:\Python\Pandas\Assignment\test_output_dataset.csv"
odi_output_file = r"D:\Python\Pandas\Assignment\od_output_dataset.csv"

# Read CSV file
df_csv = pd.read_csv(csv_file)

# Read JSON file
with open(json_file, "r") as f:
    json_data = [json.loads(line) for line in f]
df_json = pd.DataFrame(json_data)

# Merge CSV & JSON data
df = pd.concat([df_csv, df_json], ignore_index=True)

# Filter invalid players (age < 15 or > 50)
df = df[(df["age"] >= 15) & (df["age"] <= 50)]

# Remove players with missing runs or wickets
df.dropna(subset=["runs", "wickets"], inplace=True)

# Assign "Player Type"
def classify_player(row):
    if row["runs"] > 500 and row["wickets"] > 50:
        return "All-Rounder"
    elif row["runs"] > 500:
        return "Batsman"
    else:
        return "Bowler"

df["Player Type"] = df.apply(classify_player, axis=1)

# Split data into ODI and Test results
df_odi = df[df["eventType"] == "ODI"]
df_test = df[df["eventType"] == "TEST"]

# Load expected output
df_test_output = pd.read_csv(test_output_file, delimiter=";", header=0)
df_odi_output = pd.read_csv(odi_output_file, delimiter=";", header=0)

df_test = df_test.iloc[:, 1:]  # Drop the first column
df_odi = df_odi.iloc[:, 1:]  # Drop the first column

print("Test Output Columns:", df_test_output.columns)
print("ODI Output Columns:", df_odi_output.columns)
print("Processed Test Data Columns:", df_test.columns)
print("Processed ODI Data Columns:", df_odi.columns)

# Compare and validate results
df_test["Result"] = df_test.apply(lambda row: "PASS" if row.equals(df_test_output.loc[df_test_output["playerName"] == row["playerName"]].squeeze()) else "FAIL", axis=1)
df_odi["Result"] = df_odi.apply(lambda row: "PASS" if row.equals(df_odi_output.loc[df_odi_output["playerName"] == row["playerName"]].squeeze()) else "FAIL", axis=1)

# Save test results
df_test.to_csv(r"D:\Python\Pandas\Assignment\code\Result\test_result.csv", index=False)
df_odi.to_csv(r"D:\Python\Pandas\Assignment\code\Result\odi_result.csv", index=False)

print("Processing complete. Test results saved.")
