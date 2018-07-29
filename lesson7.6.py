#-*- coding:utf-8 -*-
import jieba
import wordcloud

'''
f = open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
print("type of ls is"+str(type(ls)))
txt = " ".join(ls)
print("type of txt is"+str(type(txt)))
w = wordcloud.WordCloud(font_path="msyh.ttf", width= 1000, height= 700, background_color= "white")
w.generate(txt)
w.to_file("grwordcloud.jpg")
'''

'''
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud( font_path = "msyh.ttf",\
width = 1000, height = 700, background_color = "white", \
max_words= 15
)
w.generate(txt)
w.to_file("grwordcloud2.png")
'''
from scipy.misc import imread
mask = imread("mask.jpg")
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud( font_path = "msyh.ttf",\
width = 1000, height = 700, background_color = "white", \
 mask = mask
)
w.generate(txt)
w.to_file("grwordcloud3.png")
