# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
first_scorer= 'Ruud Gullit'
second_scorer='Marco van Basten'
space= ' '
coma=', '
exclam='!'
goal_0=32
goal_1=54
scorers=(first_scorer)+(space)+str(goal_0)+(coma)+second_scorer+(space)+str(goal_1)
report=f'{first_scorer} scored in the {goal_0}nd minute\n{second_scorer} scored in the {goal_1}th minute'
player='Frank Rijkaard'
first_name=player[:5]
last_name=player[6:14]
last_name_len=len(last_name)
name_short=player[:1]+'.'+(space)+last_name
chant=((first_name)+exclam+space)*4+(first_name+exclam)
good_chant=(chant!=7)
