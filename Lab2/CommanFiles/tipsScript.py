import pandas as pd

df = pd.read_csv("tips.csv")
df = df[['tip', 'sex']]

import plotly.express as px
fig=px.histogram(df,x='sex',y='tip',histfunc='avg')
fig.show()


        