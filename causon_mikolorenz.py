import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

student_info = {
    "name": ["Kuromi", "Melody", "Cinnamoroll", "Hello Kitty"],
    "course": ["IT", "Fine Arts", "Engineering", "Theatre Arts"],
    "year_level": [3, 1, 4, 2],
    "section": [1, 3, 5, 7],
    "midterm": [100, 95, 92.5, 90],
    "final": [100, 90, 95, 100]
}

dataframe = pd.DataFrame(student_info)
dataframe["average_grade"] = (dataframe["midterm"] + dataframe["final"]) / 2
average_data = dataframe["average_grade"].to_numpy()

mean = np.mean(average_data)
median = np.median(average_data)
standard_deviation = np.std(average_data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {standard_deviation}")

student_names = dataframe["name"].to_numpy()
plt.bar(student_names, average_data, color = "blue")
plt.title("Average Grades Per Student", fontsize=14)
plt.xlabel("Student Name")
plt.ylabel("Average Grade")

plt.show()

midterm_grades = dataframe["midterm"].to_numpy()
final_grades = dataframe["final"].to_numpy()
plt.scatter(midterm_grades, final_grades, color = "green", marker = "o")
plt.title("Midterm vs Final Grades")

plt.show()

dataframe.to_csv("causon_data.csv", index=False)