import pandas as pd
import numpy as np

data = {
    "nom": ["jone", "marc", "eliot"],
    "age": [30, 35, 20],
    "travaille": ["informatique", "maçon", "ingénieur"]
}

f=np.array([50,60,70,80])
e = pd.DataFrame(data)

print(e.info())        
print(e.tail(2))
print(e.columns)

e["date"] = pd.to_datetime(["2020", "2021", "2022"])

e.set_index("date", inplace=True)  
print(e)
print(f)
e.to_excel()
