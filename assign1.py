import pandas as pd
import numpy as np

df = pd.DataFrame({'ship_mode': ['Same Day', 'First Class', 'Standard Class', 'Other'],
                   'sales': [100, 200, 300, 400],
                   'profit': [10, 20, 30, 40]})

df['surcharge'] = np.where(df['ship_mode'] == 'Same Day', 0.2,
                         np.where(df['ship_mode'] == 'First Class', 0.1,
                                  np.where(df['ship_mode'] == 'Standard Class', 0.05, 0)))

df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])

print(df)