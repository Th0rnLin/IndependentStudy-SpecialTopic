def run(ads, cas, cls, inj):
    # set goal list
    goal = {
        'address':{
            '鄉鎮市': '', #*
            '街路': '', #*
            '段': '',
            '巷': '',
            '弄': '',
            '號': '',
            '樓': ''
        },
        'case': '',
        'injured_num': 0
    }

    # response flag
    goal_address_township = False
    goal_address_road = False
    goal_case = False
    goal_injured_num = False

    counter = 1

    while counter:
      # input
      text = input()

      # update dictionary
      intent_address_flag = False
      intent_case_flag = False

      if counter == 1: intent = cls.predict(text) # predict intent => address_case, address, case
                                                  # only counter == 1

      if 'address' in intent:
        intent_address_flag = True
      if 'case' in intent:
        intent_case_flag = True

      if intent_address_flag: # address
        #address_dict = ads.get_address(text)
        for key, val in ads.get_address(text).items():
          if val: goal['address'][key] = val

      if intent_case_flag or goal_address_township or goal_address_road: # case & injured_num
        if goal['case'] is '':
          case = cas.predict(text)
          goal['case'] = case
        injured_num = inj.get_num_injured(text)
        goal['injured_num'] = str(injured_num)
      
      # update response flag
      if goal['address']['鄉鎮市']:
        goal_address_township = True

      if goal['address']['街路']:
        goal_address_road = True
        
      if goal['case']:
        goal_case = True

      if goal['injured_num']:
        goal_injured_num = True

      # response
      if not goal_address_township and not goal_address_road:
        intent = 'address'
        print('請問地點在哪')
      elif not goal_address_township and goal_address_road: # ask for township
        intent = 'address'
        print('請問是哪個地區')
        goal_address_township = True
      elif goal_address_township and not goal_address_road: # ask for road
        intent = 'address'
        print('請問是哪條路')
        goal_address_road = True
        
      elif not goal_case:
        intent = 'case'
        print('請問發生什麼事')
        goal_case = True
        
      elif not goal_injured_num:
        intent = 'case'
        print('有多少人需要救護車')
        goal['injured_num'] = 0
        goal_injured_num = True
      
      # end
      else:
        print('感謝您的報案')
        break;

      counter += 1
      
    print(goal)

if __name__ == '__main__':
    run(ads, cas, cls ,inj)
    print('finish')
