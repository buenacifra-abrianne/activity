import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

average_np = df['Average'].to_numpy()
mean_avg = np.mean(average_np)
median_avg = np.median(average_np)
std_avg = np.std(average_np)

print("Mean Average:", mean_avg)
print("Median Average:", median_avg)
print("Standard Deviation:", std_avg)

plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Average'], color='blue')
plt.title("Average Grades per Student")
plt.xlabel("Name")
plt.ylabel("Average Grade")
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df['Midterm'], df['Final'], color='red', marker='o')
plt.title("Midterm vs Final Grades")
plt.xlabel("Midterm Grade")
plt.ylabel("Final Grade")
plt.grid(True)
plt.tight_layout()
plt.show()

df.to_csv('managbanag_data.csv', index=False)
