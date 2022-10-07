from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import imageio.v2 as imageio

texto = {'a': 13,
    'b': 10,
    'c': 3
}

image = imageio.imread('brasil.png')

wordcloud = WordCloud(colormap=None, width=600, height=400, mask=image).generate_from_frequencies(texto)

plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis('off')

wordcloud.to_file('/Users/gustavocampanha/Desktop/bear.jpg')