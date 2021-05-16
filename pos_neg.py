# -*- coding: utf-8 -*-
from snownlp import SnowNLP

l = ["卧槽", "牛逼", "他妈的", "打死你", "优秀", "哈哈哈哈哈啊哈", "好评", "信不信我弄死你啊", "强强强强强强强强"]

# 保存情感极性值小于等于0.3的结果为负面情感结果
f1 = open('neg.txt', 'w', encoding='utf-8')

# 保存情感极性值大于0.3的结果为正面情感结果
f2 = open('pos.txt', 'w', encoding='utf-8')

for j in l:
    s = SnowNLP(j)
    if s.sentiments <= 0.4:
        f1.write(j + '\t' + str(s.sentiments) + '\n')
    else:
        f2.write(j + '\t' + str(s.sentiments) + '\n')
f1.close()
f2.close()
