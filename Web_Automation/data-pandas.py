import pandas as pd
data=[
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}       
    
]
df=pd.DataFrame(data)
print(df)
age=df[df['Age']]
print(age)
