import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

notas = pd.read_csv("ratings.csv")
notas.head()
notas.shape
notas.columns = ["usuarioId","filmesId","nota","momento"]
notas.head()
notas.nota
notas['nota'].unique()
notas['nota'].value_counts()
notas['nota'].mean()
# notas.nota.plot(kind='hist')
# plt.show()

# print(notas['nota'].mean())
# print(notas['nota'].median())
# print(notas.nota.describe())

sns.boxplot(notas.nota)
plt.show()
