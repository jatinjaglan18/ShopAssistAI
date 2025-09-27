import pandas as pd
from functions import product_map_layer
import openai


#Run this code once to extract product info in the form of a dictionary
laptop_df= pd.read_csv('laptop_data.csv')

## Create a new column "laptop_feature" that contains the dictionary of the product features
laptop_df['laptop_feature'] = laptop_df['Description'].apply(lambda x: product_map_layer(x))

laptop_df.to_csv("updated_laptop.csv",index=False,header = True)