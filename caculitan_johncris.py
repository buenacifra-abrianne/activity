import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Create the DataFrame
data = {
    'Name': ['Caculitan', 'Corpuz', 'Capilitan', 'Cordova'],
    'Course': ['BSIT', 'BSIT', 'BSIT', 'BSIT'],
    'Year Level': [2, 2, 2, 2],
    'Section': [1, 1, 1, 1],
    'Midterm': [95, 90, 89, 87],
    'Final': [88, 91, 88, 89]
}

df = pd.DataFrame(data)

# 2. Compute average and add new column
df['Average'] = (df['Midterm'] + df['Final']) / 2

# 3. Use NumPy to compute statistics
avg_np = df['Average'].to_numpy()
print("Mean:", np.mean(avg_np))
print("Median:", np.median(avg_np))
print("Standard Deviation:", np.std(avg_np))

# 4. Bar Chart - Average Grades per Student
plt.bar(df['Name'], df['Average'], color='skyblue')
plt.title("Average Grades per Student")
plt.xlabel("Student")
plt.ylabel("Average Grade")
plt.tight_layout()
plt.show()

# 5. Scatter Plot - Midterm vs Final Grades
plt.scatter(
    df['Midterm'], df['Final'],
    color='green', marker='o', s=50
)
plt.title("Midterm vs Final Grades")
plt.xlabel("Midterm")
plt.ylabel("Final")

# Add names just below each point
for i in range(len(df)):
    plt.text(
        df['Midterm'][i],
        df['Final'][i] - 0.5,
        df['Name'][i],
        fontsize=9,
        ha='center',
        color='black'
    )

plt.tight_layout()
plt.show()

# 6. Save cleaned data to CSV
df.to_csv("caculitan_data.csv", index=False)
