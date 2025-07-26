import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating DataFrame
students = {'name': ["Kuromi", "Melody", "Cinnamoroll", "Hello Kitty"],
            'course': ["IT", "Fine Arts", "Engineering", "Theatre Arts"],
            'year-level': [3, 1, 4, 2],
            'section': [1, 3, 5, 7],
            'midterm': [100, 95, 92.5, 90],
            'final': [100, 90, 95, 100]}
df = pd.DataFrame(students)

# New column for average grade
df['average'] = (df['midterm'] + df['final']) / 2

# Compute mean, median, and standard deviation
mean = np.mean(df['average'])
median = np.median(df['average'])
std_dev = np.std(df['average'])

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")

# create a bar chart
plt.figure(figsize=(7, 5))
plt.bar(df['name'], df['average'], color='teal')
plt.title('Average Grades per Student')
plt.xlabel('Student')
plt.ylabel('Average Grade')
plt.tight_layout()
plt.show()

#create a scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(df['midterm'], df['final'], color='teal', marker='*')
plt.title('Midterm vs Final Grades')
plt.xlabel('Midterm Grade')
plt.ylabel('Final Grade')
plt.tight_layout()
plt.show()

#save the cleaned data
df.to_csv("franco_data.csv", index=False)