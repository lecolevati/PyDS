import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

filmes = pd.read_csv("movies.csv")
filmes.columns = ["filmeId","titulo","generos"]

notas = pd.read_csv("ratings.csv")
notas.columns = ["usuarioId","filmesId","nota","momento"]

#Sem o to_string(), o PyCHarm mostra os resultados colapsados
# print(filmes.head().to_string())
# print(notas.head().to_string())

# print(notas.query("nota==1").to_string())
# print(notas.query("filmesId==1").nota.to_string())
# print(notas.query("filmesId==1").nota.mean())

# print(notas.groupby("filmesId").mean()["nota"].to_string())
# print(notas.groupby("filmesId").mean().nota.to_string())

media_por_filme = notas.groupby("filmesId").mean().nota
# media_por_filme.plot(kind='hist')
# plt.show()

# sns.boxplot(media_por_filme)
plt.figure(figsize=(3,2))
sns.boxplot(y=media_por_filme)
plt.show()

# print(media_por_filme.describe())

# sns.displot(media_por_filme, bins = 10)
# plt.show()

# plt.hist(media_por_filme)
# plt.title("Média das avaliações")
# plt.show()

