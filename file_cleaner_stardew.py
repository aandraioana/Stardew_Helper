# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:22:48 2024

@author: IugaA2
"""

import pandas as pd
import numpy as np
df = pd.read_csv("crops_raw_data.csv")
#remove columns that are mostly empty (60%) and we don't need them
print (df.isin([' ',np.nan,0]).mean())
df = df.loc[:, df.isin([' ',np.nan,0]).mean() < .6]
#update with 1.6 updates
df.rename(columns={df.columns[0]:"index"}, inplace=True)
carrot=['43','3','43','Carrot Seeds','52','A fast-growing, colorful tuber that makes for a great snack.','','','70','35','','Artisan (+40%)','8 Farming XP','Spring','','Carrot']
carrot = pd.DataFrame(columns=df.columns, data=[carrot])
squash=['44','6','56','Summer Squash Seeds','67','A curved yellow squash that is harvested while immature, and still tender.','','','90','45','','Artisan (+40%)','8 Farming XP','Summer','','Squash']
squash = pd.DataFrame(columns=df.columns, data=[squash])
broccoli=['45','8','87','Broccoli Seeds','105','The flowering head of a broccoli plant. The tiny buds give it a unique texture.','','','140','70','','Artisan (+40%)','8 Farming XP','Autumn','','Broccoli']
broccoli = pd.DataFrame(columns=df.columns, data=[broccoli])
powdermelon=['46','7','75','Powdermelon Seeds','90','Named for the powdery coating that forms on the surface, this melon is crisp and sweet, with a delicate flavor.','','','120','60','','Artisan (+40%)','8 Farming XP','Winter','','Powdermelon']
powdermelon = pd.DataFrame(columns=df.columns, data=[powdermelon])
df = pd.concat([df, carrot], axis=0)
df = pd.concat([df, broccoli], axis=0)
df = pd.concat([df, squash], axis=0)
df = pd.concat([df, powdermelon], axis=0)
energy = pd.read_csv("energy_crops.csv")
df = pd.merge(df,energy, left_on=['name'],right_on=['Name'],how='inner').drop(columns=['Name'])
multiple = pd.read_csv('multiple_harvest.csv')
df=pd.merge(df,multiple, left_on=['name'],right_on=['Name'],how='left').drop(columns=['Name','Unnamed: 3'])
df['Chance for extra'].replace(np.nan, '0%',inplace=True)
df['Multiple Harvest Count'].replace(np.nan, '1',inplace=True)
df['general_store_price'].replace(np.nan, '0', inplace=True)
df['general_store_price'].replace("", '0', inplace=True)
print(df)
df.to_csv('out_crops.csv', index=False)