import numpy as np
import jieba
from joblib import load

class Classifier:
  def __init__(self, ):
    self.p = {0: 'address_case', 1: 'case', 2: 'address'}
    self.vectorterms = []
    self.svm_linear = load('database/svm_data/SVM_linear.pkl')

    f = open('database/svm_data/vectirterms.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.vectorterms.append(i.replace('\n', ''))
    f.close()

  def __jieba_tokenizer(self, text):
    words = jieba.cut(text)
    return ' '.join([word for word in words])

  def __vectorize(self, words):
    self_main_list = [0] * len(self.vectorterms)
    for term in words:
        if term in self.vectorterms:  ## 測試資料集當中的字不一訂有出現在訓練資料集中
            idx = self.vectorterms.index(term)
            self_main_list[idx] += 1
    return np.array(self_main_list)

  def predict(self, text):
    words = self.__jieba_tokenizer(text)
    vec = self.__vectorize(words)
    return self.p[int(self.svm_linear.predict([vec]))]
