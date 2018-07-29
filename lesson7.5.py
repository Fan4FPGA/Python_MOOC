#-*- coding:utf-8 -*-
'''
wordcloud 库的使用
wordcloud把词云当作一个对象WordCloud对象
wordcloud.WordCloud() 代表一个文本对应的词云
可以根据文中词语出现的频率等参数绘制词云
绘制词云的形状，尺寸颜色都可以设定
'''
'''--------------------------------------------------------------------
wordcloud库的常规方法
w = wordcloud.WordCloud()
以WordCloud对象为基础
配置参数、加载文本、输出文件

w = wordcloud.WordCloud()
w.generate(txt)         #向WordCLoud对象w中加载文本txt
w.generate("Python and WordCLoud")

w.to_file(filename)     #将词云输出为图像文件 .png或.jpg格式
w.to_file(xxx.png)
  
  
文本 -> 分隔：以空格分隔单词 -> 统计：单词出现的频率并过滤 -> 字体：根据统计配置字号 -> 布局：颜色环境尺寸 -> 词云

配置对象参数
width = 指定词云生成的宽度 默认为400像素                  wordcloud.WordCloud(width = 400)
height = 指定词云生成的高度 默认为200像素                 wordcloud.WordCloud(height = 400)
min_font_size = 指定词云中最小字体的字号，默认为4号       wordcloud.WordCloud(min_font_size =2)
max_font_size = 指定词云中最大字体的字号                  wordcloud.WordCloud(max_font_size =20)
font_step = 指定词云中字体字号步进间隔，默认为1           wordcloud.WordCloud(font_step =2)
font_path = 指定字体文件的路径，默认为none                wordcloud.WordCloud(font_path ="msyh.ttf")
max_words = 指定词云显示最大单词数量，默认为200           wordcloud.WordCloud(max_words =20)
stop_words = 指定词云的排除字列表，即不现显示单词的列表   wordcloud.WordCloud(stop_words ={"Python","xxx"})
mask 指定词云的形状，默认为长方形，需要引用 imread()函数  form scipy.misc import imread() mk = imread("pic.png") wordcloud.WordCloud(mask = mk)
background_color 指定词云背景色，默认为黑色               wordcloud.WordCloud(background_color = "white")
------------------------------------------------------------------------'''
'''
import wordcloud
w = wordcloud.WordCloud()
w.generate("Gaoyue and FanDongshan")
w.to_file("wordcloud.png")
'''

import jieba
import wordcloud
txt = "2016年4月14日，科比·布莱恩特在生涯最后一场主场对阵爵士的常规赛后宣布退役。\
2017年12月19日，湖人主场对阵勇士，中场时刻为科比的8号和24号2件球衣举行了退役仪式。\
2018年3月13日，科比凭借和动画师格兰·基恩合作的短片《亲爱的篮球》获得第90届奥斯卡\
最佳短片奖。"
w = wordcloud.WordCloud(width=1000,height=800,max_font_size=200,min_font_size=40,\
                        font_path="msyh.ttf",font_step= 10,max_words= 50,background_color="white")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("wordcloud.jpg")
print("0")
