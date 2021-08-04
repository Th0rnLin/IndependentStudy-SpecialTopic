from chatbot_init import *

while(True):
  # end from max round
  if counter == max_round:
    print('請不要惡作劇')
    goal = {
        'address':{
            '鄉鎮市': '', #*
            '街路': '', #*
            '段': '',
            '巷': '',
            '弄': '',
            '號': '', #*
            '樓': ''},
        'case': '',
        'injured_num': ''}
    break

  # update goal list
  if update_goal_list_flag:
    output, intent = response()
    text = input(output)
    text = zh2digit(text)
    if not counter:
      first(text)
    else: second(text, intent)

  # update token
  update_address_first_flag()
  update_goal_list_flag = True

  # confirm the answer
  while(True):
    try:
      output_, intent_ = rorw_response()
      text_ = input(output_)
      text_ = zh2digit(text_)
      intent_ = update_or_not(text_, intent_)
      if intent_ == 'continue':
        break
      if len(text_)>1:
        second(text, intent)
        update_goal_list_flag = False
      if not intent_: break
    except: break

  # print goal list
  print('round : {}'.format(counter))
  print(goal)
  print('\n')

  # end from goal
  if end_from_goal() or fire_trap_falg:
    print('感謝你的報案')
    break
  # end from keyword
  if text == 'end': break
  
  # to count
  counter += 1

print('final goal => {}'.format(goal))
