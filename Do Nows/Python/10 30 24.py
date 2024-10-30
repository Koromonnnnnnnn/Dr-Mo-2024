import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Numpy Code

matrix = np.random.randint(1, 101, size=(4, 4))
print("Generated Matric:\n", matrix)

max_value = np.max(matrix)
print("Maximum Value:", max_value)

min_value = np.min(matrix)
print("Minimum Value:", min_value)

# Pie Chart / MatPlotLib

sizes = [25, 35, 15, 25]
labels = ["Category 1", "Category 2", "Category 3", "Category 4"]

plt.pie(sizes, labels=labels)
plt.title("Basic Pie Chart")
plt.show()

# Bar Graph / MathPlotLib
causes = [
    "Hardware projects",
    "Half-Eaten Snacks",
    "Mysterious Sticky Notes",
    "Enoch",
    "Papers That Blew Off the Desk",
]
items_count = [0, 5, 10, 7, 12]

plt.bar(causes, items_count, color=["orange", "green", "blue", "purple", "red"])
plt.xlabel("Causes of Mess")
plt.ylabel("Number of Items")
plt.title("Why Mo's Classroom is Messy: A Scientific Study")

plt.xticks(rotation=30, ha="right")

plt.show()

# Pandas 1

data = {
    "Friend": ["Melissa", "Natalie", "Ezri"],
    "Favorite Candy": ["Chocolate Bar", "Candy Corn", "Gummy Bears"],
    "Number Eaten This Week": [5, 3, 10],
}

df = pd.DataFrame(data)
print("Candy Preferences DataFrame:")
print(df)

# Pandas 2

scores_data = {
    "Student": ["Gus", "Liam", "Jayden"],
    "Test 1 Score": [-5684, -9245, -8947],
    "Test 2 Score": [-8584, -8855, -7505],
}

scores_df = pd.DataFrame(scores_data)
print("Students Test Scores DataFrame:")
print(scores_df)

scores_df["Average Score"] = (scores_df["Test 1 Score"] + scores_df["Test 2 Score"]) / 2
print(scores_df)

failed_students = scores_df[scores_df["Average Score"] < 60]
print("\nStudents Who Failed (Average Score Below 60):")
print(failed_students)
