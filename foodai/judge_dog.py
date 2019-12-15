import pandas as pd
import numpy as np

class=['cabbage','onion','carrot','japaneseradish','tomato']
class_class=len(class)


#judge=pd.DataFrame({'0':['犬に与えても問題ありません'],'1':['犬に与えても問題ありません'],'2':['犬に与えても問題ありません'],'3':['犬に与えてはいけません'],'4':['犬に与えてはいけません']})
#judge=pd.DataFrame({'cabbage':['犬に与えても問題ありません'],'tomato':['犬に与えても問題ありません'],'japaneseradish':['犬に与えても問題ありません'],'carrot':['犬に与えてはいけません'],'onion':['犬に与えてはいけません']})

def judge_veg(pred):
    return judge.iloc[0,pred]
