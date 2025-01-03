import pandas as pd

df = pd.read_excel('C:/Users/eugen/Downloads/Titanic.xlsx')
# Test 1: Correlation between # Family members and Survival Rate
# Test 2: Correlation between Age and Survival Rate
df = df[['Survived', 'SibSp', 'Parch', 'Age']] 
for x in df.index:
    if df.loc[x, 'Survived'] == 'Yes':
        df.loc[x, 'Survived'] = 1
    else:
        df.loc[x, 'Survived'] = 0
for x in df.index:
    if df.loc[x, 'Age'] == '-':
        df.loc[x, 'Age'] = 0
df = df.corr()
print(df.to_string())