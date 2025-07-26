import numpy as np
import pandas as pd
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

df['Average'] = np.mean([df['Midterm'], df['Final']], axis=0)

mean_avg = np.mean(df['Average'])
median_avg = np.median(df['Average'])
std_avg = np.std(df['Average'])

print("=== Grade Statistics ===")
print(f"Mean Average: {mean_avg:.2f}")
print(f"Median Average: {median_avg:.2f}")
print(f"Standard Deviation: {std_avg:.2f}\n")

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
bars = plt.bar(df['Name'], df['Average'], color=['#9b59b6', '#3498db', '#f1c40f', '#e74c3c'])
plt.title('Average Grades', fontweight='bold')
plt.xlabel('Student Name', fontweight='bold')
plt.ylabel('Average Grade', fontweight='bold')
plt.xticks(rotation=15)
plt.ylim(85, 100)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}',
             ha='center', va='bottom')

plt.subplot(1, 2, 2)
colors = ['#9b59b6', '#3498db', '#f1c40f', '#e74c3c']
plt.scatter(df['Midterm'], df['Final'], c=colors, s=200, alpha=0.8)
plt.title('Midterm vs Final Grades', fontweight='bold')
plt.xlabel('Midterm Grade', fontweight='bold')
plt.ylabel('Final Grade', fontweight='bold')
plt.xlim(85, 105)
plt.ylim(85, 105)

for i, txt in enumerate(df['Name']):
    plt.annotate(txt, (df['Midterm'][i]+0.5, df['Final'][i]+0.5))

plt.tight_layout()
plt.show()

output_filename = 'morales_data.csv'
df.to_csv(output_filename, index = False)
print(f"Data successfully saved to '{output_filename}'")