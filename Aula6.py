import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

filmes = pd.read_csv("movies.csv")
filmes.columns = ["filmeId","titulo","generos"]

notas = pd.read_csv("ratings.csv")
notas.columns = ["usuarioId","filmesId","nota","momento"]

notas_toy_story = notas.query("filmesId == 1")
notas_jumanji = notas.query("filmesId == 2")
# print(len(notas_toy_story), len(notas_jumanji))
# print("Média das Notas do Toy Story = %.2f" % notas_toy_story.nota.mean())
# print("Média das Notas do Jumanji = %.2f" % notas_jumanji.nota.mean())
#
# print("Mediana das Notas do Toy Story = %.2f" % notas_toy_story.nota.median())
# print("Mediana das Notas do Jumanji = %.2f" % notas_jumanji.nota.median())
#
# print("Desvio Padrão das Notas do Toy Story = %.2f" % notas_toy_story.nota.std())
# print("Desvio Padrão das Notas do Jumanji = %.2f" % notas_jumanji.nota.std())
#
# print("Média das Notas do Toy Story = %.2f" % notas_toy_story.nota.mean())
# print("Média das Notas do Jumanji = %.2f" % notas_jumanji.nota.mean())
#
# print("Mediana das Notas do Toy Story = %.2f" % np.median(notas_toy_story.nota))
# print("Mediana das Notas do Jumanji = %.2f" % np.median(notas_jumanji.nota))
#
# print("Desvio Padrão das Notas do Toy Story = %.2f" % np.std(notas_toy_story.nota))
# print("Desvio Padrão das Notas do Jumanji = %.2f" % np.std(notas_jumanji.nota))

# print (np.array([2.5] * 10))
# print (np.array([2.5] * 10).mean())
# print (np.append(np.array([2.5] * 10), np.array([3.5] * 10)))

filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))
filme2 = np.append(np.array([1] * 10), np.array([5] * 10))
print("Média filme 1 : ",filme1.mean())
print("Média filme 2 : ",filme2.mean())
print("Mediana filme 1 : ",np.median(filme1))
print("Mediana filme 2 : ",np.median(filme2))
print("Desvio Padrão filme 1 : ",np.std(filme1))
print("Desvio Padrão filme 2 : ",np.std(filme2))

# sns.distplot(filme1)
# sns.distplot(filme2)
# plt.show()

#distplot tá ficando depracted e deve sumir
# sns.histplot(filme1)
# sns.histplot(filme2)
# plt.show()

# plt.hist(filme1)
# plt.hist(filme2)
# plt.show()

# plt.boxplot([filme1, filme2])
# plt.show()

# plt.boxplot([notas_toy_story.nota, notas_jumanji.nota])
# plt.show()

# sns.boxplot(x="filmesId", y="nota", data=notas.query("filmesId in [1,2,3,4,5]"))
# plt.show()


