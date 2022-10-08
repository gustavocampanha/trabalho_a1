import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pergunta_4(df_artist):
    ## Separa e trata apenas colunas relevantes ao tema
    shorter_five = df_artist.sort_values(by='song_duration').head(n=5)
    longer_five = df_artist.sort_values(by='song_duration', ascending=False).head(n=5)
    return shorter_five, longer_five

def plt_pergunta_4_mais_longas(df_rank):
    df_rank = df_rank.reset_index(level = 0)
    plot = sns.barplot(data=df_rank, y="song", x="song_duration", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    plot.set( xlabel='Duração', ylabel='Música', title='Top 5 Mais Longas')
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta4_a.png') 
    # plt.show()

def plt_pergunta_4_menos_longas(df_rank):
    df_rank = df_rank.reset_index(level = 0)
    plot = sns.barplot(data=df_rank, y="song", x="song_duration", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    plot.set( xlabel='Duração', ylabel='Música', title='Top 5 Menos Longas')
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta1_4_b.png') 
    # plt.show()