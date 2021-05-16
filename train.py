# -*- coding: utf-8 -*-
import pandas as pd
from snownlp import sentiment

"""结果分别加入到 csv 文件中，然后进行模型训练，保存的路径是默认分词模块的路径，它会覆盖掉原来的 .marshal 模型文件"""

def train_model():
    data = pd.read_csv(r"./DataSet.csv", header=0)
    train = data.iloc[:40000, [1, 2]]
    test = data.iloc[40000:, [1, 2]]
    train_neg = train.iloc[:, 1][train.label == 0]
    train_pos = train.iloc[:, 1][train.label == 1]
    train_neg.to_csv(r"./neg.csv", index=0, header=0)
    train_pos.to_csv(r"./pos.csv", index=0, header=0)
    test.to_csv(r"./TestModel.csv", index=0, columns=['label', 'review'])
    sentiment.train(r'./neg.csv', r'./pos.csv')
    sentiment.save(r'C:/ProgramData/Miniconda3/Lib/site-packages/snownlp/sentiment/sentiment.marshal')


if __name__ == '__main__':
    train_model()
