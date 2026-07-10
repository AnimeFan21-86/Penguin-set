import pandas as pd
import numpy as np
import matplotlib as plt

from palmerpenguins import load_penguins
df = load_penguins()
print(df.head())
mass_avg = df.groupby("sex")["body_mass_g"].mean() #filters out sex and then corresponding mass
print(mass_avg)
mass_avg.plot(kind='bar')




