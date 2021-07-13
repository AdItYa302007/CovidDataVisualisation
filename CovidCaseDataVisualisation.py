import pandas as pd
import plotly.express as px

df=pd.read_csv("CovidData.csv")
#fig=px.line(df,x="Year",y="Per capita income",color="Country")
#fig.show()
#fig=px.bar(df,x="Country",y="InternetUsers")
fig=px.scatter(df,x="Date",y="Cases",color="Country",size_max=60)
fig.show()