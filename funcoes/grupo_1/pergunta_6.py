import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plt_correlacao_duracao_popularidade(df_artist):
    ## Gráfico de relação com o seaborn traçando as linhas onde pode ter uma diferenciação.
    plot = sns.relplot(
        data=df_artist,
        x="song_duration", y="song_rank" 
    )
    plot.set(xlabel='Duração', ylabel='Popularidade',
       title='Popularidade x Duração')
    plt.axvline(460, c='k', lw=1)
    plt.axhline(550000, c='k', lw=1)
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta1_6.png') 
    # plt.show()