import numpy as np
import pandas as pd

import os
for dirname, _, filenames in os.walk('/kaggle/input') :
   for filename in filenames:
      print(os.path.join(dirname, filename))
      
import matplotlib.pyplot as plt

pd.set_option('mode.chained_assignemnt' , None)

data = pd.read_csv("/kaggle/input/sf-air-traffic-landing-statistics/Air_Traffic_Landings_Statistics.csv")

data["Aircraft Version].replace('-', np.nan, inplace = True)
   
data.head()
   

