import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pergunta_2(df_artist):
    ## Separa e trata apenas colunas relevantes ao tema
    results_df = {
        "album": [],
        "mais_longa": [],
        "menos_longa": [],
        "mais_longa_rank": [],
        "menos_longa_rank": []
    }
    distinct_albuns = df_artist["album"].unique()
    for album in distinct_albuns:
        analysed_album = df_artist.query(f"album == '{album}'")
        first = f"{ analysed_album.sort_values(by='song_duration').head(n=1).to_numpy()[0][1] } ({album[0:20]})"
        first_rank = analysed_album.sort_values(by='song_duration').head(n=1).to_numpy()[0][3]
        last = f"{analysed_album.sort_values(by='song_duration', ascending=False).head(n=1).to_numpy()[0][1]} ({album[0:20]})"
        last_rank = analysed_album.sort_values(by='song_duration', ascending=False).head(n=1).to_numpy()[0][3]
        results_df["album"].append(album)
        results_df["mais_longa"].append(last)
        results_df["mais_longa_rank"].append(last_rank)
        results_df["menos_longa"].append(first)
        results_df["menos_longa_rank"].append(first_rank)
    results_df = pd.DataFrame.from_dict(results_df)
    return results_df

def plt_pergunta_2_mais_longas(df_rank):
    df_rank = df_rank.reset_index(level = 0)
    df_rank.drop(columns=["album","menos_longa", "menos_longa_rank", "index"],inplace = True)
    df_rank = df_rank.sort_values(by='mais_longa_rank', ascending=False)
    plot = sns.barplot(data=df_rank, y="mais_longa", x="mais_longa_rank", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    plot.set(title='Mais longas por álbum')
    plot.set( xlabel='Duração', ylabel='Música (álbum)',
       title='Mais longas por álbum')
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta1_2_a.png') 
    # plt.show()

def plt_pergunta_2_menos_longas(df_rank):
    df_rank = df_rank.reset_index(level = 0)
    df_rank.drop(columns=["album","mais_longa", "mais_longa_rank", "index"],inplace = True)
    df_rank = df_rank.sort_values(by='menos_longa_rank', ascending=False)
    plot = sns.barplot(data=df_rank, y="menos_longa", x="menos_longa_rank", color = 'g', orient='h', 
                        errorbar=("pi", 0), width=0.5)
    plot.set(title='Menos longas por álbum')
    plot.set( xlabel='Duração', ylabel='Música (álbum)',
       title='Menos longas por álbum')
    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('./respostas/pergunta1_2_b.png') 
    # plt.show()