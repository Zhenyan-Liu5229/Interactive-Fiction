scenes = {
    'beginning':{
    'description':'''You woke up. 
    It’s ten to one in the afternoon. A normal Friday afternoon, plain and dull as ever.
    You were sitting inside a computer lab, alone. Thirty computers were your only companion.
    You were very anxious. You were supposed to have the last workshop for ENG342, but no one appeared. 
    No, there was no one. No Dave or David. 
    The computer screen in front of you shone brightly, requiring a username and a password.
    ''',
    'paths':[
    {'do':'enter', 'phrase':'enter your username'},
    {'do':'shut_down', 'phrase':'shut down the computer'}
    ]
},

    #ending 1: whether to enter the username or not
    'shut_down':{
    'description':'''You thought you probably got the class time wrong. You were so exausted by arduous readings for ENG242 last night.
    Better to shut down the computer and leave.
    It would take you twenty minutes to walk back to your flat.
    I need some sleep... ''',
    'paths':[]
},

    'enter':{
    'description':'''The password was automatically filled in as soon as you typed your username.
    You were amazed. You thought you were a cautious person who never allowed public computers to remember your password.
    Just as you were wondering, one shadowy hand reached out from the computer screen and dragged you towards it. 
    What were you going to do?
    ''',
    'paths':[
    {'do':'subdue', 'phrase':'do nothing.'},
    {'do':'resist','phrase':'try your best to resist.'}
    ]
},

    #ending 2: whether to resist or not. Added on 11/04/2017
    'subdue':{
    'description':'''You did not want to resist.
    Instead, you were curious about what would happen next.
    After all, better an adventure than nothing!
    Then -- you were teleported into another world.
    ''',
    'paths':[
    {'do':'start','phrase':'look aorund'}
    ]
},
    
    'resist':{
    'description':'''You did not want to be captured away.
    You did not want to leave this world though you still had lots of work to do.
    You gathered up all your strength to fight.
    Time stopped.
    You lost yourself in this fight, forever.
    ''',
    'paths':[]
},
    # up revised 2017.11.04

    'start':{
    'description':'''You were standing in the center of a mystic world.
    Around you are digital screens marked with numbers.
    There are three screens you can choose to look at.
    PS. You can also try the random mode!
    ''',
    'paths':[
    {'do':'No.2', 'phrase':'Look at No.2'},
    {'do':'No.3', 'phrase':'Look at No.3'},
    {'do':'No.7', 'phrase':'Look at No.7'},
    {'do':'random', 'phrase':'Look at a random screen'}
    ]
},

    #The Stanley parable
    'No.7':{
    'description':'''Workshop7 -- The Stanley Parable
    You are playing The Stanley Parable. 
    Now your character, Stanley, is facing two open doors. 
    A loud male voice is repeating “Stanley chooses the door on his left”. 
    Are you going to obey him?
    ''',
    'paths':[
    {'do':'obey', 'phrase':'Move Stanley to the left door'},
    {'do':'disobey', 'phrase':'Move Stanley to the right door'}
    ]
},
    'obey':{
    'description':'''The voice is so compelling that you unconsciously obey him.
    You move Stanley through the left door. 
    You are in the world center again.
    Looks like obedience is always right.
    ''',
    'paths':[
    {'do':'No.3', 'phrase':'Look at No.3'},
    {'do':'No.5', 'phrase':'Look at No.5'},
    {'do':'No.10', 'phrase':'Look at No.10'},
    {'do':'random', 'phrase':'Look at a random screen'}
    ]
},
    'disobey':{
    'description':'''You are a person of strong free will.
    Obey a commanding stranger like him?
    Never!
    Stanley walks through the right door and never comes back. 
    ''',
    'paths':[]
}, #consider modifying it into a loop (right door == loope several times and ultimately never comes back)

    #hypertext 253
    'No.3':{
    'description':'''Workshop3 -- Hypertext
    You are reading 253, a hypertext about a London underground train. 
    There is a map of passengers in car 2 of that train. 
    Each passenger has his/her interests written below his/her name.
    ''',
    'paths':[
    {'do':'passenger63', 'phrase':'select passenger 63'}, 
    {'do':'passenger41', 'phrase':'select passenger 41'}, 
    {'do':'close_screen', 'phrase':'close the screen'}
    ]
},
    'passenger63':{
    'description':'''Passenger 63:Oliver Maskey. For more information, visit http://www.ryman-novel.com/car2/63.htm.\
    I hope you will find it interesting!''',
    'paths':[]
},
    'passenger42':{
    'description':'''Passenger 41:Mr Chris Green. For more information, visit http://www.ryman-novel.com/car2/41.htm\
    I hope you will find it interesting!
    And I tell you --
    that the train will crash in the end.''',
    'paths':[]
},
    'close_screen':{
    'description':'''You decide not to read this hypertext. You don't like to read and click.
    Instead, you turn around, and look at other screens.''',
    'paths':[
    {'do':'No.2', 'phrase':'Look at No.2'},
    {'do':'No.4', 'phrase':'Look at No.4'},
    {'do':'No.10', 'phrase':'Look at No.10'},
    {'do':'random', 'phrase':'Look at a random screen'}
    ]
},
    
    #telescopic texts
    'No.2':{
    'description':'''Workshop2 -- Telescopic Text
    You are writing a telescopic text. 
    For your sake, please do not visit http://www.telescopictext.org/text/kEVYF0kNK18qY. 
    When you finish reading, screen No.2 is replaced by No.5.
    ''',
    'paths':[
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'No.9','phrase':'Look at No.9'},
    {'do':'No.10','phrase':'Look at No.10'},
    {'do':'random', 'phrase':'Look at a random screen'}
    ]
},
    
    #Shadow of Colussus
    'No.5':{
    'description':'''Workshop5 -- Game and Narratives I 
    You are playing Shadow of Colossus, an exciting PS4 game.
    This is the first time you play with a Joystick.
    Of course, you are not playing for fun.
    You need to write a 2500-word essay about it.
    ''',
    'paths':[
    {'do':'No.3','phrase':'Look at No.3'},
    {'do':'No.6','phrase':'Look at No.6'},
    {'do':'random', 'phrase':'Look at a random screen'},
    ]
},
    
    #The God of War
    'No.6':{
    'description':'''Workshop6 -- Game and Narratives II 
    Another game? Yeah!
    This time you are playing The God of War.
    It is too hard to control the character.
    You are very distressed.
    So how about playing with texts instead of games?
    ''',
    'paths':[
    {'do':'No.1','phrase':'Look at No.1'},
    {'do':'No.7','phrase':'Look at No.7'},
    {'do':'random', 'phrase':'Look at a random screen'},
    ]
},
    
    #Interactive fiction
    'No.9':{
    'description':'''Workshop9 -- Interactive Fiction 
    Hey, isn't Interactive Fiction similar to RPGs?
    Can you solve the puzzle in Winchester's Nightmare?
    (Listen to the shell first!)
    Oh god, you spoil my game! You must pay for it!
    Do what I tell you to do!
    Now, press 1!
    ''', #add stanley parable thing into it
    'paths':[
    {'do':'No.4','phrase':'Look at No.4'},
    {'do':'No.5','phrase':'Look at No.5'},
    {'do':'random', 'phrase':'Look at a random screen'},
    ]
},
    
    #Digital poetry
    'No.4':{
    'description':'''Workshop4 -- Digital Poetry
    Poetry.
    You said to yourself.
    You are never going to like it.
    Although thoses flying words look funny.
    Although you,
    Cannot understand them.
    ''',   
    'paths':[
    {'do':'No.1','phrase':'Look at No.1'},
    {'do':'No.2','phrase':'Look at No.2'},
    {'do':'No.6','phrase':'Look at No.6'},
    {'do':'random', 'phrase':'Look at a random screen'},
    ]
},
    
    #MUDs
    'No.10':{
    'description':'''Workshop10 -- MUDs
    Role-playing! I like it!
    Emmmm.How about a wood elf with a pet wolf?
    Wait, you there, you can't eat my wolf!
    And whoever pretending to be the god, I suppose you need a rest?
    ''',
    'paths':[
    {'do':'No.3','phrase':'Look at No.3'},
    {'do':'No.4','phrase':'Look at No.4'},
    {'do':'No.6','phrase':'Look at No.6'},
    {'do':'random', 'phrase':'Look at a random screen'}
    ]
},
    
    #first workshop
    'No.1':{
    'description':'''Workshop1 -- Tactile Narratives
    Well, the beginning of workshops.
    You are very nervous, because you know you are going to introduce yourself to other students.
    I am just an exchange student. What am I supposed to say?
    Surprisingly, Dave remembers your name after this very first class!
    ''',
    'paths':[
    {'do':'No.11','phrase':'Look at No.11'},
    {'do':'random', 'phrase':'Look at a random screen'}
    ]
},
    
    #last workshop
    'No.11':{
    'description':'''Workshop11 -- Final Assembly
    Welcome to the Final Web Project Assembly.
    You are taught to create links to other students'work.
    Is that the end? You ask yourself.
    'Yes, it is.'
    You have to leave.
    ''',
    'paths':[]
},

    'random':{}
}
