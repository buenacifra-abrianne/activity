import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Name': ['Kuromi', 'Melody', 'Cinnamoroll', 'Hello Kitty'],
    'Course': ['IT', 'Fine Arts', 'Engineering', 'Theatre Arts'],
    'Year Level': [3, 1, 4, 2],
    'Section': [1, 3, 5, 7],
    'Midterm': [100, 95, 92.5, 90],
    'Final': [100, 90, 95, 100]
}

df = pd.DataFrame(data)

df['Average'] = (df['Midterm'] + df['Final']) / 2

average_array = df['Average'].to_numpy()

mean_avg = np.mean(average_array)
median_avg = np.median(average_array)
std_avg = np.std(average_array)

print(f"Mean of Averages: {mean_avg}")
print(f"Median of Averages: {median_avg}")
print(f"Standard Deviation of Averages: {std_avg}")

plt.figure(figsize=(7, 4))
plt.bar(df['Name'], df['Average'], color='skyblue')
plt.title('Average Grades per Student')
plt.xlabel('Student Name')
plt.ylabel('Average Grade')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(df['Midterm'], df['Final'], color='purple')
plt.title('Midterm vs Final Grades')
plt.xlabel('Midterm Grade')
plt.ylabel('Final Grade')
plt.grid(True)
plt.tight_layout()
plt.show()

df.to_csv('lopez_data.csv', index=False)