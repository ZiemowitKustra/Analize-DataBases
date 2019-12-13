import pandas as pd

df = pd.read_csv("/Users/Ziemek/Documents/GitHub/Analize-DataBases/Lab1/AnalysisData/pawConverted.csv", encoding="latin-1", sep='`')

#taking only income and religions collumn
df = df[['income', 'q16']]

#sort religions
religions = sorted(set(df['q16']))

#we group by income df table
grouped = df.groupby(['income'])


newTable = pd.DataFrame(columns=['Income', religions])


for name, group in grouped:
    temp_tab = [name]
    for rel in religions:
        a = pd.DataFrame(group['q16'].value_counts())
        if rel in set(group.q16):
            temp_tab.append(group.q16.count(rel))

#now we can see informations how many people from each religion has specific income
print(newTable)



