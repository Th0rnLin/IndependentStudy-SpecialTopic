import gensim
import jieba
import numpy as np

class Cases:
  def __init__(self, ):
    self.model = gensim.models.Word2Vec.load('database/word2vec_data/word2vec.model')
    
    self.disaster_rescue = []
    self.fire = []
    self.first_aid = []
    self.other = []

    f = open('database/disaster_keywords_data/災害搶救.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.disaster_rescue.append(i.replace('\n', ''))
    f.close()

    f = open('database/disaster_keywords_data/火災.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.fire.append(i.replace('\n', ''))
    f.close()

    f = open('database/disaster_keywords_data/緊急救護(救護車).txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.first_aid.append(i.replace('\n', ''))
    f.close()

    f = open('database/disaster_keywords_data/緊急救護(消防車).txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.first_aid.append(i.replace('\n', ''))
    f.close()

    f = open('database/disaster_keywords_data/其他(抓動物).txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.other.append(i.replace('\n', ''))
    f.close()

    self.keyword_dicts = [self.fire, self.disaster_rescue,  self.other, self.first_aid]
    ###
    jieba.set_dictionary('database/jieba_data/dict.txt')
    jieba.load_userdict('database/jieba_data/mydict.txt')
    ###
    self.weight2case = {
        0:'火災',
        1:'災害搶救',
        2:'其他',
        3:'緊急救護'}
    
  def __jieba_tokenizer(self, text):
    words = jieba.cut(text)
    return [word for word in words]

  def __get_simwords(self, words):
    '''
    :words => jiebaed text
    :sim_dict => # word: [sim_rate, keyword]
    '''
    sim_dict = dict()# word: [sim_rate, keyword]
    for keyword_dict in self.keyword_dicts:
      for keyword in keyword_dict:
        for word in words:
          try: sim_rate = self.model.similarity(word, keyword)
          except: sim_rate = 0
          try:
            if sim_dict[word][0] < sim_rate:
              sim_dict[word] = [sim_rate, keyword]
          except: sim_dict[word]=[0, '']
    return sim_dict

  def __get_keywords(self, sim_dict):
    simwords_val = np.array(list(sim_dict.values()))
    keywords = []
    for sim_rate, keyword in simwords_val:
      if sim_rate == simwords_val[simwords_val.argmax(axis=0)[0]][0]:
        keywords.append(keyword)
    return keywords

  def __get_case(self, keywords): #word similarity based
    keyword_weight = []
    for keyword in keywords:
      for id, keyword_dict in enumerate(self.keyword_dicts):
        if keyword in keyword_dict:
          keyword_weight.append(id)
          break
    return self.weight2case[min(keyword_weight)]

  def __get_case_(self, text): #rule based
    case = []
    for idx, keyword_dict in enumerate(self.keyword_dicts):
      for keyword in keyword_dict:
        if keyword in text:
          case.append(self.weight2case[idx])
    return case[0]

  def predict(self, text):
    try: pred = self.__get_case_(text)
    except: pred = []
    if not pred:
      words = self.__jieba_tokenizer(text)
      sim_dict = self.__get_simwords(words)
      keywords = self.__get_keywords(sim_dict)
      pred = self.__get_case(keywords)
    return pred
