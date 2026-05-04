import os
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("data.csv")

# Remove extra spaces from column names (important for safety)
df.columns = df.columns.str.strip()

# Calculate Total and Average
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Function to assign grades
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    else:
        return "C"

# Apply grading
df["Grade"] = df["Average"].apply(grade)

# Create folder for saving charts
os.makedirs("images", exist_ok=True)

# ------------------ Bar Chart ------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/bar_chart.png")
plt.show()

# ------------------ Pie Chart ------------------
plt.figure(figsize=(6, 6))
grade_counts = df["Grade"].value_counts()
plt.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.tight_layout()
plt.savefig("images/pie_chart.png")
plt.show()

# ------------------ Line Chart ------------------
plt.figure(figsize=(8, 5))
plt.plot(df["Name"], df["Total"], marker="o")
plt.title("Total Marks Trend")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/line_chart.png")
plt.show()

# Save updated data
df.to_csv("output.csv", index=False)

print("Charts saved in 'images' folder and updated data saved as 'output.csv'")