import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Name": ["Kuromi", "Melody", "Cinnamoroll", "Hello Kitty"],
    "Course": ["IT", "Fine Arts", "Engineering", "Theatre Arts"],
    "Year Level": [3, 1, 4, 2],
    "Section": [1, 3, 5, 7],
    "Midterm": [100, 95, 92.5, 90],
    "Final": [100, 90, 95, 100]
}

df = pd.DataFrame(data)
df["Average"] = (df["Midterm"] + df["Final"]) / 2

mean = np.mean(df["Average"])
median = np.median(df["Average"])
standard_dev = np.std(df["Average"])

print("==== STATISTICS ====")
print(f"Mean:               {round(mean, 2)}")
print(f"Median:             {round(median, 2)}")
print(f"Standard Deviation: {round(standard_dev, 2)}")
print("====================\n")

plt.figure(figsize=(6, 5))
bars = plt.bar(df["Student Name"], df["Average"], color='blue')
plt.title("Average Grades per Student", fontweight='bold')
plt.xlabel("Student Name", fontweight='bold')
plt.ylabel("Average Grade", fontweight='bold')
plt.xticks(rotation=15)
plt.ylim(85, 100)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.1f}",
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 5))
plt.scatter(
    df["Midterm"],
    df["Final"],
    color='darkorange',
    s=100,
    edgecolors='black'
)

for i in range(len(df)):
    plt.text(
        df["Midterm"][i] + 0.3,
        df["Final"][i],
        df["Name"][i],
        fontsize=9
    )

plt.title("Midterm vs Final Grades", fontweight='bold')
plt.xlabel("Midterm Grade", fontweight='bold')
plt.ylabel("Final Grade", fontweight='bold')
plt.grid(True)
plt.tight_layout()
plt.show()

df.to_csv("gulles_data.csv", index=False)