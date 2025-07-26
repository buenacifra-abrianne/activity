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