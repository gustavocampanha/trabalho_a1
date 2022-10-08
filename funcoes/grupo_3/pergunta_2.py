import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plt_correlacao_duracao_fans(df_albuns):
    plot = sns.relplot(
        data=df_albuns,
        x="duration", y="fans" 
    )
    plot.set(xlabel='Duração', ylabel='Fans',
       title='Popularidade x Fans')
    plt.axvline(9050, c='k', lw=1)
    plt.axhline(75000, c='k', lw=1)
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta3_2.png') 
    # plt.show()