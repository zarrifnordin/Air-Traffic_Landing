import numpy as np 
import pandas as pd

import os
for dirname, _, filenames in os.walk('/kaggle/input/sf-air-traffic-landing-statistics/Air_Traffic_Landings_Statistics.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('mode.chained_assignment', None)
   




