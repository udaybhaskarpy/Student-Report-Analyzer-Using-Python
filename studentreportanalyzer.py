import numpy as np
import pandas as pd

Names=["Uday","Aman","Naman","Badal"]
Maths=[67,54,60,89]
Science=[87,56,43,89]
English=[54,38,96,54]

dicti={
    "Names":Names,
    "Maths":Maths,
    "Science":Science,
    "English":English
}


df=pd.DataFrame(dicti)

df["Average"]=np.round(df[["Maths","Science","English"]].mean(axis=1),2)


df["Result"]=np.where(df["Average"]>=40,"Pass","Fail")

conditions=[
df["Average"]>=75,
(df["Average"]>=60) & (df["Average"]<75),
(df["Average"]>=40) & (df["Average"]<60)]

choices=["A","B","C"]

df["Grade"]=np.select(conditions,choices,default="Fail")

def Top_performer(df):
    print(df[df["Grade"]=="A"])
    
print("      ---STUDENTS REPORT---")
print()
print(df)
print()

print("      ×××GRADE (A) STUDENTS×××")

print()
Top_performer(df)

print()

print("      | | | TOP STUDENTS | | |")
print()

print(df.sort_values("Average",ascending=False).head(3))
