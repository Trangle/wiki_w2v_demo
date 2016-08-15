# wiki_w2v_demo
* 使用jieba+gensim对wiki的中英文语料做的一个简单word2vec demo，中文维基部分使用lanconv.py+zh_wiki.py这两个个文件，放入python安装目录Lib下即可
* wiki语料下载地址https://dumps.wikimedia.org/

## 直达号
* 英文 https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
* 中文 https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

## 步骤
1. 语料处理：对于英文python process_wiki.py enwiki-latest-pages-articles.xml.bz2 wiki.en.text，对于中文要进行繁体->简体转换，去掉process_wiki.py下的注释（# output.write(space.join([Converter('zh-hans').convert(x.decode('utf-8')) for x in text]).encode('utf-8') + "\n")），并注释掉output.write(space.join(text)+ "\n")，执行python process_wiki.py zhwiki-latest-pages-articles.xml.bz2 wiki.zh.text
2. 分词：运行fenci.py，更改函数read_file_cut_single相应路径和文件名
3. 执行word2vec：以中文为例python train_word2vec_model.py wiki.zh.text.seg wiki.zh.text.model wiki.zh.text.vector
4. 测试：import gensim->gensim.models.Word2Vec.load('wiki.zh.text.model')->result = model.most_similar(u'圣斗士')->for x in result: print x[0],x[1]

## 额外福利
* 如果你对分词和简繁转换不太关心，那么直接下载分词后的结果将是个不错的选择（链接：http://pan.baidu.com/s/1c9QzvC 密码：ny2m）

----
*Enjoy It!
