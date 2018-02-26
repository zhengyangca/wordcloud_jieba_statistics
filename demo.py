# coding:utf-8

from os import path
import chnSegment
import plotWordcloud


if __name__=='__main__':

    # Load source file
    d = path.dirname(__file__)
    text = open(path.join(d,'doc//2017年中央政府工作报告(全文).txt')).read()

    # segment words via jieba
    text=chnSegment.word_segment(text)

    # generate and plot Word Cloud
    plotWordcloud.generate_wordcloud(text)
