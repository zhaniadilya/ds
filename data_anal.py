import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
#%matplotlib inline     
sns.set(color_codes=True)

df = pd.read_csv("C:/Users/Alser/OneDrive/Документы/SU documents/mtcars")
# To display the top 5 rows 
df.head(5) 

df.tail(5) 

df.dtypes

df = df.drop(['hp', 'drat', 'wt', 'qsec', 'vs', 'am'], axis=1)
df.head(5)

df = df.rename(columns={"model": "car_model", "mpg": "Miles Per Gallon", "hp": "Horsepower"})
df.head(5)

df.shape

duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

df.count()

df = df.drop_duplicates()
df.head(5)

df.count()

print(df.isnull().sum())

df = df.dropna()    # Dropping the missing values.
df.count()

print(df.isnull().sum())   # After dropping the values

sns.boxplot(x=df['drat'])

sns.boxplot(x=df['Horsepower'])

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape

df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make')

plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['Horsepower'], df['drat'])
ax.set_xlabel('Horsepower')
ax.set_ylabel('drat')
plt.show()