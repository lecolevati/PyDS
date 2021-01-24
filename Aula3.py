import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

tmdb = pd.read_csv("tmdb_5000_movies.csv")
# print(tmdb.head().to_string())
# print(tmdb.original_language.unique())

# print(tmdb.original_language.value_counts())
# print(tmdb.original_language.value_counts().index)
# print(tmdb.original_language.value_counts().values)
# print(tmdb.original_language.value_counts().to_frame())
# print(tmdb.original_language.value_counts().to_frame().reset_index())

contagens_de_linguas = tmdb.original_language.value_counts().to_frame().reset_index()
contagens_de_linguas.columns = ["original_language", "total"]
# print(contagens_de_linguas.head())

# plt.figure(figsize=(10, 5))
# sns.barplot(x="original_language", y="total", data=contagens_de_linguas)
# plt.show()

# sns.catplot(x="original_language", kind="count", data=tmdb)
# plt.show()

# plt.pie(contagens_de_linguas["total"], labels = contagens_de_linguas["original_language"])
# plt.show()

total_por_lingua = tmdb.original_language.value_counts()
# print(total_por_lingua.loc["en"])
total_geral = total_por_lingua.sum()
total_ingles = total_por_lingua.loc["en"]
total_outros = total_geral - total_ingles
# print(total_ingles, total_outros)

dados = {
    'lingua' : ['ingles', 'outros'],
    'total' :  [total_ingles, total_outros]
}

# print(dados)

dados = pd.DataFrame(dados)
# print(dados.to_string())

# plt.figure(figsize=(7,4))
# plt.title("Total de filmes por idioma")
# sns.barplot(x="lingua", y="total", data=dados)
# plt.show()

# plt.pie(dados["total"], labels = dados["lingua"])
# plt.show()

# print(tmdb.query("original_language == 'en'"))
# print(tmdb.query("original_language != 'en'"))

filmes_nao_ingles = tmdb.query("original_language != 'en'")
total_por_lingua_outros = filmes_nao_ingles.original_language.value_counts()
# print(total_por_lingua_outros)

sns.catplot(x="original_language", kind="count", data=filmes_nao_ingles,
            aspect=2, palette="GnBu_d", order=total_por_lingua_outros.index)
plt.show()

# contagens_de_linguas_nao_ingles = filmes_nao_ingles.original_language.value_counts().to_frame().reset_index()
# contagens_de_linguas_nao_ingles.columns = ["original_language", "total"]
# plt.figure(figsize=(10, 5))
# sns.barplot(x="original_language", y="total", data=contagens_de_linguas_nao_ingles)
# plt.show()
