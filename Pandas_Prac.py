import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Name': ['Alice', 'Brian', 'Chloe'],
    'Age': [20, 22, 19],
    'Grade': [65, 45, 78]
}

#print the dataframe

df = pd.DataFrame(data)

#print the dataframe
print("All students: ")
print(df)

# Step 2: Add "Passed" column
df['Passed'] = df['Grade'] > 50

# Step 3: Filter and display only students who passed
passed_students = df[df['Passed']]

print("Students who passed:")
print(passed_students)
