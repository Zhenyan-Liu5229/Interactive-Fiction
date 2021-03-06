from Scene import scenes
import sys
import random
import numpy as np

def print_header():
    print('''
    _            _      _             _                  _     _        
   /_\  _ _     /_\  __| |_ _____ _ _| |_ _  _ _ _ ___  (_)_ _| |_ ___  
  / _ \| ' \   / _ \/ _` \ V / -_) ' \  _| || | '_/ -_) | | ' \  _/ _ \ 
 /_/_\_\_||_| /_/ \_\__,_|\_/\___|_||_\__|\_,_|_| \___| |_|_||_\__\___/ 
 |   \(_)__ _(_) |_ __ _| | | |  (_) |_ ___ _ _ __ _| |_ _  _ _ _ ___   
 | |) | / _` | |  _/ _` | | | |__| |  _/ -_) '_/ _` |  _| || | '_/ -_)  
 |___/|_\__, |_|\__\__,_|_| |____|_|\__\___|_| \__,_|\__|\_,_|_| \___|  
        |___/    
        ''')

def readstatus(screens): #for users to check which contents they have read
    if screens not in read_status:
        read_status.append(screens)
    return(read_status)

def savestatus(): #save and load (2017.8.24)
    status_save = np.array(read_status)
    np.save('save.npy', status_save)
    print('Data saved!')


read_status = []
numbers = [1,2,3,4,5,6,7,9,10] #The number of each screen

#start of the game    
print_header()
print('''

Welcome to An Adventure into Digital Literature!
You are one of students enrolled in ENG342 paper.
Now, your adventure starts...
''')

delay = input('>>> Press ENTER to start <<<')


#the default beginning scene
scene = scenes['beginning'] #notice: the scene is actually scenes[scene] instead of the name of that sence
while True:
    next_step = None    
    description = scene['description']
    paths  = scene['paths']
    print(scene['description'])


#Review the choices on board
    for i in range(0,len(paths)):
        path = paths[i]
        menu_item = i+1
        print(menu_item, path['phrase'])
    print('\n(r, To view what you have read)\n(s, To save your progress)\n(l, To load your saved progress)\n(0, To quit the game)')


#User selection
    prompt = 'Make a selection (0-%s):' %len(paths)
    while next_step == None:
        try:
            step = input(prompt)
            if step == 'r': #what the user has read
                print('''*************************************
-- You have read %s''' %read_status)
            elif step == 's': #save progress
                savestatus()
            elif step == 'l': #load progress
                next_step = 'load'
                print('Data loaded!')
            else: 
                menu_selection = int(step)   
                if menu_selection == 0:
                    next_step = 'quit the game' #quit the game
                else:
                    index = menu_selection-1 #other normal selection
                    next_step = paths[index]

        except (IndexError,ValueError):
            print(step,'is not a valid selection!',)

    if next_step == 'quit the game': #quit the game
        print('\nYou decided to %s. Good Bye!' %next_step)
        sys.exit()
    elif next_step == 'load': #load the game
        read_status = np.load('save.npy')
        scene = scenes[read_status[-1]]
    else: #normal selection
        scene = scenes[next_step['do']]
        next_phrase = str.lower(next_step['phrase'])
        readstatus(next_step['do'])
        print('''*************************************
You decided to %s.''' %next_phrase)
        
        if scene == {}: #random mode
            screen_number = random.choice(numbers)
            numbers.remove(screen_number)
            new_screen = 'No.'+ str(screen_number)
            scene = scenes[new_screen]
            readstatus(new_screen)
            if numbers == []:
                scene = scenes['No.11']
                readstatus('No.11')
