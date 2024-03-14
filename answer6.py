# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VAtbsPNBDwnUfsupyOukHTgSMXfasWod
"""

import pandas as pd

df=pd.read_csv("/content/country_vaccination_stats.csv")

df

top_3_countries = df.groupby('country')['daily_vaccinations'].median().nlargest(3)

top_3_countries