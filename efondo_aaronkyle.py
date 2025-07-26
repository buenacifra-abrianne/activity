import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

student_info = {
    'name': ["Kuromi", "Melody", "Cinnamoroll", "Hello Kitty"],
    'course': ["IT", "Fine Arts", "Engineering", "Theatre Arts"],
    'year_level': [3, 1, 4, 2],
    'section': [1, 3, 5, 7],
    'midterm': [1.00, 1.50, 1.75, 2.00],
    'final': [1.00, 2.00, 1.50, 1.00]
}

df = pd.DataFrame(student_info)
df['average'] = (df['midterm'] + df['final']) / 2 

average = df['average'].to_numpy()

mean_value = np.mean(average)
median_value = np.median(average)
std_value = np.std(average)

print(f"Mean Value: {mean_value}")
print(f"Median Value: {median_value}")
print(f"Standard Deviation Value: {std_value}")

name = df['name']

plt.bar(name, average, color="blue", width=0.3)
plt.title("Student Average Grades")
plt.xlabel('Students')
plt.ylabel('Average Grades')
plt.grid(True)
plt.show()

midterm_score = df['midterm'].to_numpy()
final_score = df['final'].to_numpy()

plt.scatter(midterm_score, final_score, color="blue", marker='s')
plt.title('Midterm vs. Final')
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")
plt.grid(True)
plt.show()

df.to_csv("efondo.csv", index=False)