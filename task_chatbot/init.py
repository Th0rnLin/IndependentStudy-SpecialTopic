from Address import Address
from Cases import Cases
from Classifier import Classifier
from Injured import Injured

def init():
    # init
    ads = Address() # ads.get_address(text) => output : {'巷': '', '弄': '', '樓': '', '段': '', '號': '', '街路': '', '鄉鎮市': ''}
    print('finish1')
    cas = Cases() # cas.predict(text) => output : '火災', '災害搶救', '其他', '緊急救護'
    print('finish2')
    cls = Classifier() # cls.predict(text) => output : 'address_case', 'case', 'address'
    print('finish3')
    inj = Injured() # inj.get_num_injured(text) => output : number
    print('finish4')
    return ads, cas, cls, inj
if __name__ == '__main__':
    init()
    print('finish')
