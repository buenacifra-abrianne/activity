import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pineda_dyanna.py
# dataframe
data = {
    "Name": ["Kuromi", "Melody", "Cinnamoroll", "Hello Kitty"],
    "Course": ["IT", "Fine Arts", "Engineering", "Theatre Arts"],
    "Year Level": [3, 1, 4, 2],
    "Section": [1, 3, 5, 7],
    "Midterm": [100, 95, 92.5, 90],
    "Final": [100, 90, 95, 100]
}

df = pd.DataFrame(data)

df["Average"] = (df["Midterm"] + df["Final"]) / 2

average_array = df["Average"].to_numpy()

mean_avg = np.mean(average_array)
median_avg = np.median(average_array)
std_avg = np.std(average_array)

print(f"Mean of Averages: {mean_avg}")
print(f"Median of Averages: {median_avg}")
print(f"Standard Deviation of Averages: {std_avg}")

# Visualization 1: Bar Chart (Average Grades per Student)
plt.figure(figsize=(8, 5))
bars = plt.bar(df["Name"], df["Average"], color="purple", alpha=0.7)
plt.title("Average Grades per Student")
plt.xlabel("Students")
plt.ylabel("Average Grade")
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)


for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height:.1f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Visualization 2: Scatter Plot (Midterm vs Final Grades)
plt.figure(figsize=(8, 5))
plt.scatter(df["Midterm"], df["Final"], color="pink", s=100, alpha=0.7,
            marker='*')
plt.title("Midterm vs Final Grades")
plt.xlabel("Midterm Grades")
plt.ylabel("Final Grades")
plt.grid(True, alpha=0.3)


for i, name in enumerate(df["Name"]):
    plt.annotate(name, (df["Midterm"].iloc[i], df["Final"].iloc[i]),
                 xytext=(5, 5), textcoords='offset points', fontsize=9,
                 alpha=0.8)

min_grade = min(df["Midterm"].min(), df["Final"].min())
max_grade = max(df["Midterm"].max(), df["Final"].max())
plt.plot([min_grade, max_grade], [min_grade, max_grade], 'k--',
         alpha=0.5, label='Midterm = Final')
plt.legend()

plt.tight_layout()
plt.show()

# Save cleaned data to CSV
df.to_csv("pineda_data.csv", index=False)