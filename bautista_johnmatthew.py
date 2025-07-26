import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

students_df = pd.DataFrame({
    "Name" : ["Kuromi", "Melody", "Cinnamoroll", "Hello Kitty"],
    "Course" : ["IT", "Fine Arts", "Engineering", "Theatre Arts"],
    "Year Level" : [3, 1, 4, 2],
    "Section" : [1, 3, 5, 7],
    "Midterm" : [100, 95, 92.5, 90],
    "Final" : [100, 90, 95, 100]
})

# Add Average column
students_df['Average'] = (students_df['Midterm'] + students_df['Final']) / 2

# Compute mean, median and std
print("Grade Averages")
print(f"Mean: {students_df['Average'].mean()}")
print(f"Median: {students_df['Average'].median()}")
print(f"Standard Deviation: {students_df['Average'].std()}")

# Bar Chart (Average grades)
plt.bar(students_df['Name'], students_df['Average'])
plt.title("Average Grades per Student")
plt.xlabel("Student Name")
plt.ylabel("Average")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Scatter Plot (Midterm vs Final grades)
plt.scatter(students_df["Midterm"], students_df["Final"], marker='D')
plt.title("Midterm vs Final Grades")
plt.xlabel("Midterm Grades")
plt.ylabel("Final Grades")
plt.grid(True)
plt.tight_layout()
plt.show()

# Save clean data
students_df.to_csv("bautista_data.csv", index=False)