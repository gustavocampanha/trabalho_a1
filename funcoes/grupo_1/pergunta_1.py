import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pergunta_1(df_artist):
    ## Separa e trata apenas colunas relevantes ao tema
    results_df = {
        "album": [],
        "mais_ouvida": [],
        "menos_ouvida": [],
        "mais_ouvida_rank": [],
        "menos_ouvida_rank": []
    }
    distinct_albuns = df_artist["album"].unique()
    for album in distinct_albuns:
        analysed_album = df_artist.query(f"album == '{album}'")
        first = f"{ analysed_album.sort_values(by='song_rank').head(n=1).to_numpy()[0][1] } ({album[0:20]})"
        first_rank = analysed_album.sort_values(by='song_rank').head(n=1).to_numpy()[0][5]
        last = f"{analysed_album.sort_values(by='song_rank', ascending=False).head(n=1).to_numpy()[0][1]} ({album[0:20]})"
        last_rank = analysed_album.sort_values(by='song_rank', ascending=False).head(n=1).to_numpy()[0][5]
        results_df["album"].append(album)
        results_df["mais_ouvida"].append(last)
        results_df["mais_ouvida_rank"].append(last_rank)
        results_df["menos_ouvida"].append(first)
        results_df["menos_ouvida_rank"].append(first_rank)
    results_df = pd.DataFrame.from_dict(results_df)
    return results_df

def plt_pergunta_1_mais_ouvidas(df_rank):
    df_rank = df_rank.reset_index(level = 0)
    # Retira colunas não utilizadas nesse gráfico
    df_rank.drop(columns=["album","menos_ouvida", "menos_ouvida_rank", "index"],inplace = True)
    df_rank = df_rank.sort_values(by='mais_ouvida_rank', ascending=False)
    # Gera gráfico de barras com dados utilizandos na horizontal
    plot = sns.barplot(data=df_rank, y="mais_ouvida", x="mais_ouvida_rank", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    # Caracteriza gráfico
    plot.set( xlabel='Popularidade', ylabel='Música (álbum)',
       title='Mais ouvidas por álbum')
    # Ajusta layout como automático para não cortar os nomes dos álbuns e músicas
    plt.rcParams.update({'figure.autolayout': True})
    # Gera imagem de resposta do gráfico
    plt.savefig('./respostas/pergunta1_1_a.png') 
    # plt.show()

def plt_pergunta_1_menos_ouvidas(df_rank):
    df_rank = df_rank.reset_index(level = 0)
    # Retira colunas não utilizadas nesse gráfico
    df_rank.drop(columns=["album","mais_ouvida", "mais_ouvida_rank", "index"],inplace = True)
    df_rank = df_rank.sort_values(by='menos_ouvida_rank', ascending=False)
    # Gera gráfico de barras com dados utilizandos na horizontal
    plot = sns.barplot(data=df_rank, y="menos_ouvida", x="menos_ouvida_rank", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    # Caracteriza gráfico
    plot.set( xlabel='Popularidade', ylabel='Música (álbum)',
       title='Menos ouvidas por álbum')
    # Ajusta layout como automático para não cortar os nomes dos álbuns e músicas
    plt.rcParams.update({'figure.autolayout': True})
    # Gera imagem de resposta do gráfico
    plt.savefig('./respostas/pergunta1_1_b.png') 
    # plt.show()