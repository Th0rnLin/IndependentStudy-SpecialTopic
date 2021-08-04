#@title 1. load some library

from address import Address
from case import Case
from injured import Injured
from rorw import RorW
from zh2digit import Zh2Digit
from digit2zh_ads import Digit2Zh_ads

# init
ads = Address() # ads.get_address(text) => output : {'巷': '', '弄': '', '樓': '', '段': '', '號': '', '街路': '', '鄉鎮市': ''}
cas = Case() # cas.predict(text) => output : '火災', '受困', '抓動物', '緊急救護'
inj = Injured() # inj.get_num_injured(text) => output : number
rorw = RorW() # rorw.get_right_or_wrong(text) => output : True or False
z2d = Zh2Digit() # z2d.zh2digit_text(text) => output : text(number => digit)
d2z_ads = Digit2Zh_ads() # d2z_ads.digit2zh(text) => output : text(number => zh)

'''

#@title 10. initization
# to count
counter = 0

# set goal list
goal = {
    'address':{
        '鄉鎮市': '', #*
        '街路': '', #*
        '段': '',
        '巷': '',
        '弄': '',
        '號': '', #*
        '樓': ''
    },
    'case': '',
    'injured_num': ''
}

# if false then representative this not confirmed
address_flag = False
case_flag = False
injured_flag = False

# token
address_first_flag = False
#update_goal_list_flag = True
fire_trap_falg = False
resp = []

max_round = 20 # need to discuss

text  = ''
text_ = ''
'''
