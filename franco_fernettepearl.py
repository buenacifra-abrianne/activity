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