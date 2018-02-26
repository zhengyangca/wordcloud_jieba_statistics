# coding:utf-8

from collections import Counter
from os import path
import jieba
jieba.load_userdict(path.join(path.dirname(__file__),'userdict//userdict.txt')) # 导入用户自定义词典

def word_segment(text):

    # cut words by white space
    jieba_word=jieba.cut(text,cut_all=False) # cut_all is false by default
    data=[]
    for word in jieba_word:
        data.append(word)
    dataDict=Counter(data)

    # output to txt file
    with open('doc//词频统计.txt','w') as fw:
        for k,v in dataDict.items():
            fw.write("%s,%d\n" % (k,v))
        #  fw.write("%s"%dataDict)


    # return segmented word list to the main process
    jieba_word=jieba.cut(text,cut_all=False) # cut_all is false by default
    seg_list=' '.join(jieba_word)
    return seg_list

