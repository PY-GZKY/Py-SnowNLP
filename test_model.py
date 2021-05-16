# -*- coding: utf-8 -*-
import pandas as pd
from snownlp import SnowNLP

if __name__ == '__main__':
    test = pd.read_csv(r"TestModel.csv")
    review_list = [review for review in test['review']]
    label_list = [label for label in test['label']]
    list_test = [(label, review) for label, review in list(zip(label_list, review_list)) if type(review) != float]

    for j in list_test:
        print(j[1], j[0], SnowNLP(j[1]).sentiments)

    senti = [SnowNLP(review).sentiments for label, review in list_test]

    newSenti = []
    for i in senti:  # 预测结果为pos的概率,大于0.6我们认定为积极评价
        if (i >= 0.6):
            newSenti.append(1)
        else:
            newSenti.append(0)

    counts = 0
    for i in range(len(list_test)):
        if (newSenti[i] == list_test[i][0]):
            counts += 1

    accuracy = float(counts) / float(len(list_test))
    print("准确率为:%.2f" % accuracy)
