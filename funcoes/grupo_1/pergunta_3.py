import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pergunta_3(df_artist):
    ## Separa e trata apenas colunas relevantes ao tema
    less_listen_five = df_artist.sort_values(by='song_rank').head(n=5)
    more_listen_five = df_artist.sort_values(by='song_rank', ascending=False).head(n=5)
    return less_listen_five, more_listen_five


def plt_pergunta_3_mais_ouvidas(df_rank):
    df_rank = df_rank.reset_index(level = 0)
    plot = sns.barplot(data=df_rank, y="song", x="song_rank", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    plot.set( xlabel='Popularidade', ylabel='Música', title='Top 5 Mais ouvidas')
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta1_3_a.png') 
    # plt.show()

def plt_pergunta_3_menos_ouvidas(df_rank):
    df_rank = df_rank.reset_index(level = 0)
    plot = sns.barplot(data=df_rank, y="song", x="song_rank", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    plot.set( xlabel='Popularidade', ylabel='Música', title='Top 5 Menos ouvidas')
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta1_3_b.png') 
    # plt.show()