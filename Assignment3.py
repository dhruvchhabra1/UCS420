

import pandas as pd

#q1
data = {
    'Tid': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Refund': ['Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'No'],
    'Marital Status': ['Single', 'Married', 'Single', 'Married', 'Divorced',
                       'Married', 'Divorced', 'Single', 'Married', 'Single'],
    'Taxable Income': [125000, 100000, 70000, 120000, 95000,
                       60000, 220000, 85000, 75000, 90000],
    'Cheat': ['No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

print(df)


#q2
print(df.loc[[0, 4, 7, 8]])


# q3.1
print("Rows from index 3 to 7:")
print(df.iloc[3:8])

# q3.2
print("\nRows from index 4 to 8 and columns 2 to 4:")
print(df.iloc[4:9, 2:5])

# q3.3
print("\nAll rows with column index 1 to 3:")
print(df.iloc[:, 1:4])


#q4
from google.colab import files

uploaded = files.upload()

df = pd.read_csv('Iris.csv')

df.head()


#q5
df = df.drop(index=4)

df = df.drop(df.columns[3], axis=1)

print(df)

#q6
data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
    'Age': [29, 34, 41, 28, 38],
    'Salary': [50000, 70000, 65000, 55000, 60000],
    'Years_of_Experience': [4, 8, 10, 3, 12],
    'Joining_Date': ['2020-03-15', '2017-07-19', '2013-06-01',
                     '2021-02-10', '2010-11-25'],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'Bonus': [5000, 7000, 6000, 4500, 5000],
    'Rating': [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pd.DataFrame(data)
df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])

df.to_csv('employees.csv', index=False)

print("a) Shape:", df.shape)

print("\nb) DataFrame Information:")
df.info()

print("\nc) Descriptive Statistics:")
print(df.describe())

print("\nd) First 5 rows:")
print(df.head(5))

print("\nLast 3 rows:")
print(df.tail(3))

print("\ne) Statistics:")
print("i. Average Salary:", df['Salary'].mean())
print("ii. Total Bonus:", df['Bonus'].sum())
print("iii. Youngest Age:", df['Age'].min())
print("iv. Highest Rating:", df['Rating'].max())

df = df.sort_values(by='Salary', ascending=False)

print("\nf) Sorted by Salary (Descending):")
print(df)

def performance_category(rating):
    if rating >= 4.5:
        return 'Excellent'
    elif rating >= 4.0:
        return 'Good'
    else:
        return 'Average'

df['Performance_Category'] = df['Rating'].apply(performance_category)

print("\ng) Performance Category:")
print(df[['Name', 'Rating', 'Performance_Category']])

print("\nh) Missing Values:")
print(df.isnull().sum())

df.rename(columns={'Employee_ID': 'ID'}, inplace=True)

print("\ni) After renaming Employee_ID to ID:")
print(df)

print("\nj(i) Employees with more than 5 years experience:")
print(df[df['Years_of_Experience'] > 5])

print("\nj(ii) Employees in IT department:")
print(df[df['Department'] == 'IT'])

df['Tax'] = df['Salary'] * 0.10

print("\nk) DataFrame with Tax:")
print(df)

df.to_csv('employees_modified.csv', index=False)

print("\nl) Modified dataset saved as employees_modified.csv")

from google.colab import files
files.download('employees_modified.csv')