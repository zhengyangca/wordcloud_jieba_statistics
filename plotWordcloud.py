# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def generate_wordcloud(text):
    # WordCloud configurations
    d=path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "Images//alice_mask.png")))
    font_path=path.join(d,"font//msyh.ttf")
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",
           max_words=2000,
           # mask=alice_mask,  
           stopwords=stopwords,
           font_path=font_path,
                  )

    wc.generate(text)

    # save word cloud to local path
    wc.to_file(path.join(d, "Images//alice.png"))

    # show window
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值

    plt.axis("off")# take off the axis of the image
    plt.show()

