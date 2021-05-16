# Py-SnowNLP
![Py-SnowNLP](https://img.shields.io/badge/Python-3.5+-green)
![Py-SnowNLP](https://img.shields.io/badge/Snownlp-0.12.3-blue)

### `Python`分词, 情感分析工具 `SnowNLP`

### 生成`模型`,预测`分类`


### 主要功能
- `中文分词`（Character-Based Generative Model）
- `词性标注`（TnT 3-gram 隐马）
- `情感分析`（现在训练数据主要是买卖东西时的评价，所以对其他的一些可能效果不是很好，待解决）
- `文本分类`（Naive Bayes）
- `转换成拼音`（Trie树实现的最大匹配）
- `繁体转简体`（Trie树实现的最大匹配）
- `提取文本关键词`（TextRank算法）
- `提取文本摘要`（TextRank算法）
- `tf, idf`
- `Tokenization`（分割成句子）
- `文本相似`（BM25）

> 现在训练数据主要是针对`电商`服务类的评价，所以对其他的一些可能效果不是很好

> 详情文章参考 [Python分词, 情感分析工具 SnowNLP](https://zhuanlan.zhihu.com/p/101493588)