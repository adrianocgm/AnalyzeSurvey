import pandas as pd
import os

OUTPUT_CSV = os.getenv('OUTPUT_CSV')

df = pd.read_csv(OUTPUT_CSV)
print (OUTPUT_CSV)
print (df)