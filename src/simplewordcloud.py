# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import jieba  #jieba分词
from wordcloud import WordCloud

def main(): 
    #制作词云的文件地址
    path_txt = 'F://ass.txt'
    #读取文件
    word = open(path_txt,'r').read()
    #剪切词语，包括汉字
    cut_txt = " ".join(jieba.cut(word)) 
    wordcloud = WordCloud(
        #避免乱码 
        font_path="C:/Windows/Fonts/simfang.ttf",
        width=800,  #设置词云宽度
        height=800,
        background_color="white",
        scale=1.5).generate(cut_txt) 
    plt.imshow(wordcloud, interpolation="bilinear") 
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()











