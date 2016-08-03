# _*_coding:utf8_*_

import sys
import re
import codecs
import os
import shutil
import jieba
import jieba.analyse

jieba.load_userdict("D:\\360Downloads\\nlp\\Ch_Seg\\dict.txt")

def test_demo1():
    text = "我来到北京清华大学"
    seg_list = jieba.cut(text, cut_all=True)
    print u"[全模式]: ", "/ ".join(seg_list)
    seg_list = jieba.cut(text, cut_all=False)
    print u"[精确模式]: ", "/ ".join(seg_list)
    seg_list = jieba.cut(text)
    print u"[默认模式]: ", "/ ".join(seg_list)
    seg_list = jieba.cut("他来到了网易杭研大厦")
    print u"[新词识别]: ", "/ ".join(seg_list)
    seg_list = jieba.cut_for_search(text)
    print u"[搜索引擎模式]: ", "/ ".join(seg_list)


# Read file and cut
def read_file_cut_single():
    # create path
    path = "D:\\360Downloads\\"
    respath = "D:\\360Downloads\\"

    fileName = path + "wiki.zh.text"
    resName = respath + "wiki.zh.text.seg"
    source = open(fileName, 'r')
    if os.path.exists(resName):
        os.remove(resName)
    result = codecs.open(resName, 'w', 'utf-8')
    line = source.readline()
    line = line.rstrip('\n')
    while line != "":
        line = unicode(line, "utf-8")
        seglist = jieba.cut(line, cut_all=False)  # 精确模式
        output = ' '.join(list(seglist))  # 空格拼接
        print output
        result.write(output + '\r\n')
        line = source.readline()
    else:
        print 'End file'
        source.close()
        result.close()

# Read file and cut
def read_file_cut():
    # create path
    path = "BaiduSpider\\"
    respath = "BaiduSpider_Result\\"
    if os.path.isdir(respath):
        shutil.rmtree(respath, True)
    os.makedirs(respath)

    num = 1
    while num <= 204:
        name = "%04d" % num
        fileName = path + str(name) + ".txt"
        resName = respath + str(name) + ".txt"
        source = open(fileName, 'r')
        if os.path.exists(resName):
            os.remove(resName)
        result = codecs.open(resName, 'w', 'utf-8')
        line = source.readline()
        line = line.rstrip('\n')

        while line != "":
            line = unicode(line, "utf-8")
            seglist = jieba.cut(line, cut_all=False)  # 精确模式
            output = ' '.join(list(seglist))  # 空格拼接
            print output
            result.write(output + '\r\n')
            line = source.readline()
        else:
            print 'End file: ' + str(num)
            source.close()
            result.close()
        num = num + 1
    else:
        print 'End All'


# Run function
if __name__ == '__main__':
    read_file_cut_single()