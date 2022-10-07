from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

def wcloud(list, img, name):

    tam = len(list)
    text = ''
    for a in range(0, tam):
        text += list[a]
        text += ' '


    python_mask = np.array(PIL.Image.open(img))
    color_map = ImageColorGenerator(python_mask)
    wc = WordCloud(stopwords=STOPWORDS, 
                mask=python_mask, 
                background_color="white",
                contour_color="black",
                contour_width=3,
                min_font_size=3).generate(text)
    wc.recolor(color_func=color_map)
    """ plt.imshow(wc)
    plt.axis("off")
    plt.show() """

    name = name + '.png'
    wc.to_file(name)