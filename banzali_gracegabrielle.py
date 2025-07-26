import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Creating DataFrame
student_info = {'name': ["Kuromi", "Melody", "Cinnamoroll", "Hello Kitty"],
                'course': ["IT", "Fine Arts", "Engineering", "Theatre Arts"],
                'year': [3, 1, 4, 2],
                'section': [1, 3, 5, 7],
                'midterm_grade': [100, 95, 92.5, 90],
                'final_grade': [100, 90, 95, 100]}

df = pd.DataFrame(student_info)

df['average'] = (df['midterm_grade'] + df['final_grade']) / 2

mean_ave = np.mean(df['average'])
median_ave = np.median(df['average'])
std_dev = np.std(df['average'])

print(f"Mean: {mean_ave}\nMedian: {median_ave}\nStandard Deviation: {std_dev}")

##### BAR CHART
plt.bar(df['name'], df['average'])
plt.bar(df['name'], df['average'], color = 'green')

plt.title("Average Grades per Student", fontsize = 18)
plt.xlabel("Student", fontsize = 12)
plt.ylabel("Average Grade", fontsize = 12)

plt.tight_layout()
plt.show()

##### SCATTER PLOT
plt.scatter(df['midterm_grade'], df['final_grade'], 
            color = 'black', marker = '*')

plt.yticks(np.arange(80, 110, 5))

plt.title("Midterm vs Final Grades", fontsize = 18)
plt.xlabel("Midterm Grade", fontsize = 12)
plt.ylabel("Final Grade", fontsize = 12)

plt.grid(True)
plt.tight_layout()
plt.show()

df.to_csv('banzali_data.csv', index=False)
