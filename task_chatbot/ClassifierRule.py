class ClassifierRule:
  def __init__(self, ):
    self.address = []

    f = open('database/address_data/township.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.address.append(i.replace('\n', ''))
    f.close()

    f = open('database/address_data/rd.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.address.append(i.replace('\n', ''))
    f.close()

    f = open('database/address_data/st.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.address.append(i.replace('\n', ''))
    f.close()

    f = open('database/address_data/other.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.address.append(i.replace('\n', ''))
    f.close()
        
    f = open('database/address_data/ln.txt', 'r', encoding='utf-8')
    for i in f.readlines():
      self.address.append(i.replace('\n', ''))
    f.close()
  def predict_rule(self, text):
    case = 'case'
    for i in self.address:
      if i[:-1] in text:
        case = 'address'
    return case
