import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# ave grade per student
df["Average"] = (df["Midterm"] + df["Final"]) / 2

# used numpy for mean, median, and standard deviation
mean_avg = np.mean(df["Average"])
median_avg = np.median(df["Average"])
std_avg = np.std(df["Average"])

print(f"Mean Average: {mean_avg}")
print(f"Median Average: {median_avg}")
print(f"Standard Deviation: {std_avg}")

# visualization #1 (Bar Chart) - ave grade per student
plt.figure(figsize=(6, 4))
plt.bar(df["Name"], df["Average"], color="red")
plt.title("Average Grades per Student")
plt.xlabel("Students")
plt.ylabel("Average Grade")
plt.show()

# visualization #2 (Scatter Plot) - midterm vs final grade
plt.figure(figsize=(6, 4))
plt.scatter(df["Name"], df["Midterm"],
            color="blue", label="Midterm", marker="o")
plt.scatter(df["Name"], df["Final"],
            color="red", label="Final", marker="x")
plt.title("Midterm vs Final")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.legend()
plt.show()

df.to_csv("corpus_data.csv", index=False)
