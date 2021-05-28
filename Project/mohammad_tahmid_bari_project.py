#!/usr/bin/env python
"""
OCR using Python by tesseract
=============================
Converting the image file into a textual format and writing it into a text file.
================================================================================
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from PIL import Image
from os import path
from wordcloud import WordCloud, STOPWORDS
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

filename = "input.txt"
f = open(filename, "w")

# converting the image file into a textual format
# writing the converted text into a file
content = pytesseract.image_to_string(Image.open('test2.png'))

f.write(content)
f.close()


# d = path.dirname(__file__)

# Read the whole text.
text = open('input.txt').read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/food/chili-pepper-1.gif
chili_mask = np.array(Image.open("chili-pepper-1.gif_595.jpg"))

stopwords = set(STOPWORDS)
stopwords.add("english")

wc = WordCloud(background_color="white", max_words=2000, mask=chili_mask,
               stopwords=stopwords,scale=4,width=800, height=400)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file("chili.png")

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.show()