# variables to store game information
current_level = 1
final_level = 5
game_completed = False
# iterate until the final level is reached
while current_level <= final_level:
    """ 
    follow condition game_completed True, following condition 
    execute when game_completed is True, otherwise below 
    condition block skipped. 
    """
    if not game_completed:  
       print (f'welcome to level {current_level}')
       current_level += 1
print("Game over!")