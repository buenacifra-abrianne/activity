import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = {
            'Name': ["Kuromi", "Melody", "Cinamoroll", "Hello Kitty"],
            'Course': ["IT", "Fine Arts", "Engineering", "Theater Arts"],
            'Year Level': [3, 1, 4, 2],
            'Section': [1, 3, 5, 7],
            'Midterm': [100, 95, 92.5, 90],
            'Final': [100, 90, 95, 100]
        }

df = pd.DataFrame(students)
df['Average'] = (df['Midterm'] + df['Final']) / 2


mean = np.mean(df['Average'])
median = np.median(df['Average'])
standard_deviation = np.std(df['Average'])

print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", standard_deviation)

plt.bar(df['Name'], df['Average'], color = 'green')

plt.xlabel('Students')
plt.ylabel('Average')
plt.title('Average Grade of Students')

plt.show()

plt.scatter(df['Midterm'], df['Final'], color = 'black', edgecolor = 'black')

plt.xlabel('Midterm')
plt.ylabel('Final')
plt.title('Comparison of Midterm and Final Grades')

plt.grid(True)
plt.show()

df['Name'] = df['Name'].str.title()
df['Course'] = df['Course'].str.title()

df.to_csv('espinola_data.csv', index = False)