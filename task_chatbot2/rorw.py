import gensim
import jieba

class RorW:
  def __init__(self, ):
    #self.model = gensim.models.Word2Vec.load('drive/MyDrive/wiki_word2vec2/word2vec.model')
    
    # use rule
    self.right_keys_r = ['是', '對', '行', '沒錯', '好', '恩']
    self.wrong_keys_r = ['不是', '不對', '不行', '否', '錯', '不好', '不'] # '不' should consider
    # use cosine similarity
    #self.right_keys_c = ['沒錯', '好']
    #self.wrong_keys_c = ['否', '錯', '不好']
  
  def __jieba_tokenizer(self, text):
    words = jieba.cut(text)
    return [word for word in words]
  
  def get_right_or_wrong(self, text):
    
    # cosine similarity
    '''
    words = self.__jieba_tokenizer(text)
    
    for word in words:
      for i in self.wrong_keys_c:
        try:
          if self.model.similarity(word, i) > 0.8:
            return True
        except: pass
      for i in self.right_keys_c:
        try:
          if self.model.similarity(word, i) > 0.8:
            return False
        except: pass
    '''
    # rule
    for i in self.wrong_keys_r:
      if i in text:
        return False

    for i in self.right_keys_r:
      if i in text:
        return True

    return None # if answer the unquestioned
