import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plt_pergunta_1_mais_fans(df_albuns):
    df_albuns = df_albuns.sort_values(by='fans')
    df_albuns = df_albuns.reset_index(level = 0)
    plot = sns.barplot(data=df_albuns, y="album", x="fans", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    plot.set( xlabel='Fans', ylabel='Álbum', title='Álbuns com mais fans da história')
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta3_1.png') 
    # plt.show()
