import streamlit
import seaborn
from matplotlib import pyplot
import pandas as pd

data={
    "students":["Arun","Ram","Anu"],
    "maths":[80,90,87],
    "science":[75,67,54]
}

df=pd.DataFrame(data)
df

pyplot.figure(figsize=(2,2))
seaborn.barplot(data=data,x="students",y="maths",palette="coolwarm")
streamlit.pyplot(pyplot)

pyplot.figure(figsize=(2,2))
seaborn.barplot(data=data,x="students",y="science",palette="coolwarm")
streamlit.pyplot(pyplot)




