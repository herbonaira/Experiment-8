import pandas as pd
cars = pd.read_csv('cars.cs')
b = cars.loc[0:4]
cars2 = b.append(cars.loc[27:31])
