import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Name': ['USAIF', 'SALMAAN', 'ABDULLAH', 'NAZAR'], 'MARK1': [80, 95, 77, 63]}
df = pd.DataFrame(data)

sns.barplot(x='Name', y='MARK1', data=df)
plt.show()
