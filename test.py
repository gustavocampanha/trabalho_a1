from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas laborum atque cumque totam unde pariatur ad amet odit, architecto magni illo fugit id sed, tempora maiores praesentium voluptate quasi quisquam?"

def wcloud(text, img):
    python_mask = np.array(PIL.Image.open(img))
    color_map = ImageColorGenerator(python_mask)
    wc = WordCloud(stopwords=STOPWORDS, 
                mask=python_mask, 
                background_color="white",
                contour_color="black",
                contour_width=3,
                min_font_size=3).generate(text)
    wc.recolor(color_func=color_map)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

wcloud(text,"img/fgvlogo.png")