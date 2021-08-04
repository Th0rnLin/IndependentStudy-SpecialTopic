class RorW:
  def __init__(self, ):
    # keywords
    self.positive = ['是', '對', '行', '好', '恩', '有', '會', '同意', '可以']
    self.negative = ['沒', '錯', '不', '否', '才', '反']
    
  def get_right_or_wrong(self, text):
    flag = False # judge this is answer
    answer = 1

    for i in text:
      if i in self.positive:
        #answer *= 1
        flag = True
      if i in self.negative:
        answer *= -1
        flag = True

    if flag:
      if answer > 0: return True
      else: return False
    else: return 'None'
