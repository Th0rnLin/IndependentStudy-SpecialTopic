import gensim
import jieba

class FirstAidKeyword:
  def __init__(self, ):
    self.model = gensim.models.Word2Vec.load('database/word2vec_data/word2vec.model')
    self.first_aid = []
    f = open('database/disaster_case_data/QAKeyword.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.first_aid.append(i.replace('\n', ''))
    f.close()
    ###
    jieba.set_dictionary('database/jieba_dict_data/dict.txt')
    jieba.load_userdict('database/jieba_dict_data/mydict.txt')
    ###
  
  def __jieba_tokenizer(self, text):
    words = jieba.cut(text)
    return [word for word in words]
  
  def get_keyword(self, text):
    max_sim_word = ''
    max_sim_rate = 0

    words = self.__jieba_tokenizer(text)
    for word in words:
      for keyword in self.first_aid:
        try:
          sim_rate = self.model.similarity(word, keyword)
          if sim_rate > max_sim_rate:
            max_sim_word = word
            max_sim_rate = sim_rate
        except: pass
    return max_sim_word, max_sim_rate
