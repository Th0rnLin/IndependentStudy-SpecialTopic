import gensim

class RorW:
  def __init__(self, ):
    # use rule
    self.special_right_key_r = ['沒錯']
    self.right_keys_r = ['是', '對', '行', '好', '恩', '有']
    self.wrong_keys_r = ['不是', '不對', '不行', '否', '錯', '不好', '不', '沒'] # '不' should consider

  def get_right_or_wrong(self, text):
    # rule
    if self.special_right_key_r[0] in text: return True
    for i in self.wrong_keys_r:
      if i in text:
        return False

    for i in self.right_keys_r:
      if i in text:
        return True

    return None # if answer the unquestioned
