from time import sleep
from random import choice, randint
import os
import sys
import pygame

pygame.mixer.init()

playlist = list()
playlist.append ( "301 - Good Memories.mp3" )
playlist.append ( "308 - The Tea Garden, Enhanced Version (Scene).mp3" )
playlist.append ( "311 - Love from Afar.mp3" )
playlist.append ( "300-A - Desecrated Temple (MP3).mp3" )

pygame.mixer.music.load ( playlist.pop(1) )  
pygame.mixer.music.queue ( playlist.pop(2) ) 
pygame.mixer.music.set_endevent ( pygame.USEREVENT )    
pygame.mixer.music.play()           



time_1 = """\n+8-=-=-=-=-=-8+
 | ,.-'"'-., |
 |/:.     .:\|
 |\:::::::::/|
 | \:::::::/ |
 |  \:::::/  |
 |   \:::/   |
 |    ):(    |
 |   / . \   |
 |  /  .  \  |
 | /   .   \ |
 |/    :    \|
 |\   .:.   /|
 | '--___--' |
+8-=-=-=-=-=-8+"""

time_2 = """\n+8-=-=-=-=-=-8+
 | ,.-'"'-., |
 |/         \|
 |\:.     .:/|
 | \:::::::/ |
 |  \:::::/  |
 |   \:::/   |
 |    ):(    |
 |   / . \   |
 |  /  .  \  |
 | /   .   \ |
 |/   .:.   \|
 |\.:::::::./|
 | '--___--' |
+8-=-=-=-=-=-8+"""

time_3 = """\n+8-=-=-=-=-=-8+
 | ,.-'"'-., |
 |/         \|
 |\         /|
 | \:.   .:/ |
 |  \:::::/  |
 |   \:::/   |
 |    ):(    |
 |   / . \   |
 |  /  .  \  |
 | /   .   \ |
 |/  .:::.  \|
 |\:::::::::/|
 | '--___--' |
+8-=-=-=-=-=-8+"""

time_4 = """\n+8-=-=-=-=-=-8+
 | ,.-'"'-., |
 |/         \|
 |\         /|
 | \       / |
 |  \:. .:/  |
 |   \:::/   |
 |    ):(    |
 |   / . \   |
 |  /  .  \  |
 | / .:::. \ |
 |/:::::::::\|
 |\:::::::::/|
 | '--___--' |
+8-=-=-=-=-=-8+"""

time_5 = """\n+8-=-=-=-=-=-8+
 | ,.-'"'-., |
 |/         \|
 |\         /|
 | \       / |
 |  \     /  |
 |   \   /   |
 |    ):(    |
 |   /.:.\   |
 |  /.:::.\  |
 | /:::::::\ |
 |/:::::::::\|
 |\:::::::::/|
 | '--___--' |
+8-=-=-=-=-=-8+"""

time_runs_out = "Your time has run out! Your kingdom is lost!"

def start():
    
    intro_splash = """\n

  _______                                          _        _____        
 |__   __|                       /\               | |      |  __ \       
    | | ___  __ _ _ __ ___      /  \   _ __  _ __ | | ___  | |__) |   _  
    | |/ _ \/ _` | '_ ` _ \    / /\ \ | '_ \| '_ \| |/ _ \ |  ___/ | | | 
    | |  __/ (_| | | | | | |  / ____ \| |_) | |_) | |  __/ | |   | |_| | 
    |_|\___|\__,_|_| |_| |_| /_/    \_\ .__/| .__/|_|\___| |_|    \__, | 
                                      | |   | |                    __/ | 
                                      |_|   |_|                   |___/  PRESENTS:\n"""

    intro_game_name = """\n
    
          ▒█████   ██    █  █████  ██▀███   █     █░ ▒█████   ██▀███   ██▓    ▓█████▄ 
         ▒██   ██  ██    █  █     ██   ██▒▓ █ █  █░▒ ██▒  ██▒▓██ ▒ ██▒▓██▒    ▒██▀ ██▌
         ▒██   ██▒  ██  █  ████   ██  ▄█ ▒▒█░ █ ░█ ▒ ██░  ██▒▓██ ░▄█ ▒▒██░    ░██   █▌
         ▒██   ██░   ██ █ ▒▓█     ██▀▀█▄  ░█░ █ ░█ ▒ ██   ██░▒██▀▀█▄  ▒██░    ░▓█▄   ▌
         ░ ████▓▒░   ▒▀█░  ░█████▒██▓ ██▒░  █████▓ ░  ████▓▒░░██▓ ▒██▒░██████▒░▒████▓ 
            ░ ▒░▒░▒░    ░  ░  ░░ ▒░ ░░ ▒  ░▒ ░░  ░▒ ▒  ░ ▒░▒░▒░ ░ ▒  ░▒ ░░ ▒░   ░ ▒▒   ▒ 
           ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░░ ░ ▒  ░ ░ ▒  ▒ 
           ░ ░ ░ ▒       ░░     ░     ░░   ░   ░   ░  ░ ░ ░ ▒    ░░   ░   ░ ░    ░ ░  ░ 
          ░ ░        ░     ░  ░   ░         ░        ░ ░     ░         ░  ░   ░    
                 ░                                                       ░     \n"""

    print(intro_splash)
    sleep(2)
    print(intro_game_name)
    sleep(4)
    os.system('cls')
    return prelogue()

# start()

def prelogue():

    prelogue_text = """\n  
    [ctrl + c to skip]
    
    ^**--- Prelogue ---**^ 
    
    For years, there had been no war, no crime, and no hardship in the Kingdom. 
    
    Peace and prosperity flowed through the kingdom for several decades.

    The right-hand of the High leader eventually became so bitter and resentful that the Great Ruler had turned so placid. 
    
    "A Sovereign is supposed to be all powerful and feared", one would think...

    ... But on one perticular day, seeking to exile and take over the High leader, the right-hand willingly paid a healthy sum of gold coins to a banished Sorceror.

    The instructions were simple. Remove the Leader, and banish them to a place of no return.

    The sorceror agreed, but under one condition - His banishment will be exonerated and he would be honoured as a citizen of the kingdom once more!

    That very night, the Sorceror infiltrated the High Leader's chambers, magically opened up a portal and exiled them to the Overworld.
    
    The kingdom panicked, a search went on for weeks, but all hope was lost as the high leader was never found.
   
    The right-hand was eventually appointed as ruler, whilst the true High Leader awoke in a dark, gloomy forest, seemlingly enclosed with a plethora of ghastly beings.

    Instinctively, they knew they were banished to the Overworld. 
    
    The forbidden books of the Overworld they had secretly enjoyed thoroughout their childhood were now a blessing.

    Magic will be their true ally..."""

    try:
        for letter in prelogue_text:
            sleep(0.04)
            sys.stdout.write(letter)
            sys.stdout.flush()
        sleep(2)    
        return checkpoint_1()
    except KeyboardInterrupt:
        os.system('cls')
        print(prelogue_text)
        sleep(2)    
        return checkpoint_1()

time_left = 24

def checkpoint_1():

    text_1 = """\n
    As you wake up in the dark, gloomy forest you are greeted with haunting sounds. 
    
    Your memory is fleeting.
    
    Your mind is uneasy.\n"""

    print(text_1)
    return name_func()
    
def name_func():
    global name
    name = input("Do you remember your name? [Please enter your name]: ")
    if len(name) > 0:
        res = input(f"\n{name}? Is that correct? [Y]/[N]: ")
        if res.lower() == "y":
            return land_name()
        elif res.lower() == "n":
            return name_func()
        else:
            print(message())
            return name_func()
    else:
        print(message())
        return name_func()

def land_name():
    global location1
    location1 = input("\nAnd which land did you arrive from? [1] Sterus [2] Frehorn or [3] Urok?: ")
    if location1 == "1":
        location1 = "Sterus"
        return pre_name()
    elif location1 == "2":
        location1 = "Frehorn"
        return pre_name()
    elif location1 == "3":
        location1 = "Urok"
        return pre_name()
    else:
        print(message())
        sleep(1)
        return land_name()

def pre_name():        
    sleep(1)
    print(f"\nGreetings {name}, High Leader of {location1} ")
    sleep(3)
    os.system('cls')
    print("             Disclaimer : YOU HAVE 24 HOURS TO ESCAPE THE OVERWORLD!!! REMEMBER THAT AN HOUR IN THE OVERWORLD IS A YEAR IN THE KINGDOM")
    print("")
    print(f"{time_left} hours remaining!")
    if time_left > 18:
        print(time_1)
    elif time_left > 12:
        print(time_2)
    elif time_left > 6:
        print(time_3)
    elif time_left > 0:
        print(time_4)
    else:
        print(time_1)
        print(time_runs_out)
        return start()
    return name_selected()

def name_selected():

    text_1 = f"""\n
    ^**--- Act 1 ---**^

    You hear a comforting voice in front of you.

    "Welcome to the dark realms of the Overworld {name} of {location1}. 
    
    This is the forest of Shadowmoss.

    I am your guide Mercearius, and I will be with you for every choice you make along the way. 

    Think of me as a spirit guide.\n"""

    print(text_1)
    return checkpoint2()

def checkpoint2():

    text_1 = f"""\n
    It seems you have been bound magically to a tree and a dark red glow emits from around your wrists.

    Mercearius tells you of 3 spells, of which one will help you escape the magic shackles.
    
    "Take a look here {name} of {location1}" he exclaims!

    \n\033[1;34;40m Mercearius' blue aura guides your eyes to an etheral scroll in front of you, with three spells

    \033[0;37;40m[1] - Exteula

    [2] - Alteraris

    [3] - Supresus\n"""

    print(text_1)
    sleep(1)
    return question1()

def question1():

    text_1 = """\nExtuela!
    
    Whoosh!


    . '@(@@@@@@@)@. (@@) `  .   '
     .  @@'((@@@@@@@@@@@)@@@@@)@@@@@@@)@ 
     @@(@@@@@@@@@@))@@@@@@@@@@@@@@@@)@@` .
  @.((@@@@@@@)(@@@@@@@@@@@@@@))@\@@@@@@@@@)@@@  .
 (@@@@@@@@@@@@@@@@@@)@@@@@@@@@@@\\@@)@@@@@@@@)
(@@@@@@@@)@@@@@@@@@@@@@(@@@@@@@@//@@@@@@@@@) ` 
 .@(@@@@)##&&&&&(@@@@@@@@)::_=(@\\@@@@)@@ .   .'
   @@`(@@)###&&&&&!!;;;;;;::-_=@@\\@)@`@.
   `   @@(@###&&&&!!;;;;;::-=_=@.@\\@@     '
      `  @.#####&&&!!;;;::=-_= .@  \\
            ####&&&!!;;::=_-        `
             ###&&!!;;:-_=
              ##&&!;::_=
             ##&&!;:=
            ##&&!:-
           #&!;:-
          #&!;=
          #&!-
           #&=
            #&-
            \\#/'
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    
    The bonds have vanished and you are now free of the tree. \n"""

    text_2 = """\nAlteraris!

    The spell works, splitting the tree half way down the middle.
    
    Although the tree is split making it easier to move you must now rely on your physical capabilities.

    You notice that only moving one arm can free you fully.
    
    With the tree split, and both your arms tensed, you have to decide which arm to move to free yourself with. \n"""

    text_5 = """\n Supresus!
        
        BOOM!!! 


     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
        

        You explode with tremendous force - you are now one with DEATH.\n"""

    quest1 = input("\nWhich number spell do you choose... [1] Exteula, [2] Alteraris, [3] Supresus?: ")
    if quest1 == "1":
        os.system('cls')
        global time_left
        time_left -= 2
        print(text_1)
        sleep(4)
        os.system('cls')
        print(f"{time_left} hours remaining")
        print(time_remaining())
        return act_2()
    elif quest1 == "2":
        os.system('cls')
        print(text_2)
        def tree_split():

            text_5 = """\n 
    You used your left arm and pulled!"""

            text_6 = """\n 
    You used your right arm!"""

            arm = input("With the tree split, and both your arms tensed, you have to decide which arm to move to free yourself. [1] being left or [2] being right: ")
            def arm_scenario():

                text_3 = """
    The tree creaks and moans, falling backwards slowly, freeing you of the tree.\n"""

                text_4 = """
    The wind catches the tree & it collapses! Flattening you!\n"""

                coin_toss = randint(0, 1)
                if coin_toss % 2 == 1:
                    global time_left
                    time_left -= 2
                    print(text_3)
                    sleep(4)
                    os.system('cls')
                    print(f"{time_left} hours remaining")
                    print(time_remaining())
                    return act_2()
                else:
                    print(text_4)
                    return q1_death()
            if arm == "1":
                print(text_5)
                return arm_scenario()
            elif arm == "2":
                print(text_6)
                return arm_scenario()
            else:
                print(message())
                return tree_split()
        return tree_split()
    elif quest1 == "3":
        os.system('cls')
        print(text_5)
        return q1_death()
    else:
        print(message())
        return question1()

def q1_death():
    global time_left
    res = input("[1] Would you like to start again? Or [2] would you like to make that decision again?: ")
    if res == "1":
        time_left = 24
        os.system('cls')
        return start()
    elif res == "2":
        # global time_left
        time_left -= 3
        os.system('cls')
        print(f"{time_left} hours remaining")
        print(time_remaining())
        return question1()
    else:
        print(message())
        return q1_death()

# This sets the scene for act 2 and establishes 2 paths
def act_2():

    act_2_text = """
    ^**--- Act 2 ---**^

    "That's right, you have magic powers in this realm. You just have to speak to them correctly" said Mercearius, "you are now free to explore and escape the forest at will".

    After Mercearius' mention of magic you compose yourself and begin to wander through the forest looking for answers and a sense of direction.

    As you continue, the pungent whiff of ancient bark and moss engulfs your nasal domain. Nevertheless, you feel cleansed internally.

    Something unidentifiable also fills the air - could it be the aura of magic itself or the atmosphere of this surreal dimension altering your perception of reality?  

    Your thoughts drift and it becomes apparent a clear path lies ahead.

    You are left with two choices now.
    Choose wisely... or it might be your last.
  
    [A] Clear Path 
    
    OR 
    
    [B] Continue through the forest\n"""

    print(act_2_text)
    sleep(1)
    select_option = input("[A] or [B]?: ")
    if select_option.lower() == "a":
        os.system('cls')
        return act_2_1()
    elif select_option.lower() == "b":
        os.system('cls')
        return act_2_2()
    else:
        print(message())
        sleep(2)
        os.system('cls')
        return act_2()

# this follows path 1 of act 2 and gives you 2 choices to progress
def act_2_1():

    act_2_1_text = f"""\n
    
    You stumble upon a gaping hole which is too large to jump across - 

    "One does believe my magic is the only solution here", suggests {name}, high leader of {location1}  
  
    Do you 
  
    [A] cast the spell Levaritus and levitate over
  
    OR

    [B] the spell Brigardea and build a magic bridge across?\n"""

    print(act_2_1_text)
    sleep(1)
    return act_2_1_choice()

# path 1 choices - success moves onto act_3 and fail restarts this function 
def act_2_1_choice():
    global time_left

    act_2_1_choice_text = """\n
    
    You float over the hollow depression embedded within the earth and make it across safely.\n"""

    act_2_1_choice_text_2 = """
    Your magic is not strong enough and the etheral bridge evaporates before your very own eyes.

    Thankfully, using your formidable agility you manage to grab and clasp onto the ledge with your dear life.

    As you clamber up onto the ledge of the hole, you consider your options. Do you cast [A] levitate or [B] the same spell?\n"""

    act_2_1_choice_text_3 = """\n 

    Your etheral bridge holds up radiantly and you make it across safely.\n"""

    select_option = input("[A] or [B]?: ")
    if select_option.lower() == "a":
        global time_left
        time_left -= 2
        print(act_2_1_choice_text)
        sleep(4)
        os.system('cls')
        return act_3()
    elif select_option.lower() == "b":
        num = randint(0, 1)
        if num % 2 == 0:
            #global time_left
            time_left -= 4
            print(act_2_1_choice_text_2)
            sleep(2)
            os.system('cls')
            # print(f"{time_left} hours remaining")
            # print(time_remaining())
            return act_2_1_choice()
        else:
            #global time_left
            time_left -= 3
            print(act_2_1_choice_text_3)
            sleep(4)
            os.system('cls')
            # print(f"{time_left} hours remaining")
            # print(time_remaining())
            return act_3()
    else:
        print(message())
        sleep(2)
        os.system('cls')
        return act_2_1()

# this follows path 2 of act 2 and gives you 2 choices to progress
def act_2_2():

    act_2_2_text = """\n 
    
    As you progress further through the forest, you catch a glimpse of an inert beast laying before you.

    This is not a scenario one would likely leave unscaved if you were to make the wrong decision.

    Do you -

    [A] Cast the spell Adtono to cause a distraction

    OR

    [B] Tread lightly and sneak past the foul monster?\n"""

    print(act_2_2_text)
    sleep(1)
    return act_2_2_choice()

# path 2 choices - success moves onto act_3
def act_2_2_choice():
    global time_left

    act_2_2_choice_text = """\n
    
    Success! - your nimbleness serves you well and you make it past without a sound.\n"""

    act_2_2_choice_text_2 = """\n 
    
    Your magic is not strong enough and the distraction becomes the very sound of you casting your spell.
    
    The wretched beast notices you kerfuffle with your incantations and leaps towards your poor soul.\n"""

    act_2_2_choice_text_3 = """\n 
    
    Your magic works perfectly and the foul beast leaps towards the echo of rustled bushes and murmurs in the distance, thus giving you right of passage.\n"""

    select_option = input("[A] or [B]?: ")
    if select_option.lower() == "b":
        global time_left
        time_left -= 2
        print(act_2_2_choice_text)
        sleep(4)
        print(f"{time_left} hours remaining")
        print(time_remaining())
        os.system('cls')
        return act_3()
    elif select_option.lower() == "a":
        num = randint(0, 1)
        if num % 2 == 0:
            #global time_left
            time_left -= 3
            print(act_2_2_choice_text_2)
            sleep(2)
            print(f"{time_left} hours remaining")
            print(time_remaining())
            return act_2_2_choice2()
        elif num % 2 != 0:
            time_left -= 2
            print(act_2_2_choice_text_3)
            sleep(2)
            print(f"{time_left} hours remaining")
            print(time_remaining())
            os.system('cls')
            return act_3()
        else:
            print(message())
            sleep(2)
            os.system('cls')
            return act_2_2()
    else:
        print(message())
        sleep(2)
        os.system('cls')
        return act_2_2()

# seperate function for coin flip in path 2 choices - success moves onto act_3 and fail means you die or restart
def act_2_2_choice2():
    global time_left

    act_2_2_choice_text_2 = """\n 
    
    Your magic is not strong enough and the distraction becomes the very sound of you casting your spell.
    
    The wretched beast notices you kerfuffle with your incantations and leaps towards your poor soul.\n"""

    act_2_2_choice2_text = """\n 
    
    Alas, as the monster leaps towards you you fail to dodge in time and are crushed to smithereens - you are now one with DEATH.\n"""

    act_2_2_choice2_text_2 = """\n 
    
    You dodge the monster, roll forward and scurry away with little to no effort.\n"""

    try:
        select_num = int(input("\nTEST YOUR AGILITY! - pick a number between 1 and 6: "))
        if select_num <= 6 and select_num % 2 != 0:
            #global time_left
            sleep(2)
            os.system('cls')
            print(act_2_2_choice2_text)
            return act_2_death()
        elif select_num <= 6 and select_num % 2 == 0:
            time_left -= 3
            print(act_2_2_choice2_text_2)
            sleep(2)
            print(f"{time_left} hours remaining")
            print(time_remaining())
            os.system('cls')
            return act_3()
        else:
            print(message())
            sleep(2)
            os.system('cls')
            print(act_2_2_choice_text_2)
            return act_2_2_choice2()
    except TypeError and ValueError:
        print(message())
        sleep(2)
        os.system('cls')
        print(act_2_2_choice_text_2)
        return act_2_2_choice2()

def act_2_death():
    res = input("[1] Would you like to start again? Or [2] would you like to make that decision again?")
    if res == "1":
        global time_left
        os.system('cls')
        time_left = 24
        return start()
    elif res == "2":
        # global time_left
        time_left -= 3
        os.system('cls')
        print(f"{time_left} hours remaining")
        print(time_remaining())
        return act_2_2_choice2()
    else:
        print(message())
        return act_2_death()

def act_3():
    
    print(f"{time_left} hours remaining")
    print(time_remaining())

    text_1 = f"""\n
    ^**--- Act 3 ---**^

    You escape the forest of Shadowmoss with all limbs intact.

    "You are a true hero afterall", Mercearius proclaims joyfully!

    You step out of the forest, and see a long crooked path leading to a sinister Mountain.

    "I know of this place!", {name} high leader of {location1} exclaims!
    
    "This is the lengendary Mount Wrath, I recognise that snowy peak from the forbidden books"
    
    Mercearius appears to you in a flash of blue light.

    "You need to climb up the mountain until you find the secret cave entrance, where you can seek the Ancient ruin"

    "It is your one and only chance of escaping this wretched world. Be wary High Leader, the path is full of grave peril"
 
    You get to the base of Mount Wrath and observe three possible ways you you could approach the climb.

    "Which path would you like to take {name}, my highness of {location1}?", asks Merearius.
    
    "And may I remind you of the dangers ahead"\n"""

    text_2 = """\n\033[1;34;40m MERCEARIUS' BLUE AURA GUIDES YOUR EYES TO THE PATHS THAT LAY AHEAD
    
    \033[0;37;40m Choose your fate!\n """

    print(text_1)
    sleep(2)
    print(text_2)
    return tablet()

def tablet(): 
    global time_left
    print("\n[1] - Left-hand path")                                                                                               
    print("[2] - Right-hand path")                                                   
    print("[3] - Attempt to climb directly up") 
    print("   ")
    response1 = input("Which numbered choice would you like to use? Press [1], [2] or [3]?: ")
    print("   ")
    # Left hand path
    if response1 == "1":  
        os.system('cls')
        #global time_left  
        print("A snarling Karkavarus leaps at you from a cave.")
        print("   ")
        print("Do you?")
        print("   ")
        print("[1] - Jump to the left?")
        print("[2] - Step backwards?")
        print("   ")
        response2 = input("Which numbered choice would you like to use? Press [1], or [2]?: ")
        print("   ")
        if response2 == "1":
            time_left -= 3
            print("The Karkavarus dives at you viciously, as you step out of the way. It falls to it's death")
            sleep(4)
            os.system('cls')
            return snow_section()        
        elif response2 == "2":
            print("You fall off the mountain edge")
            print("   ") 
            print("You die!!!")
            print("   ")    
            return act_3_death()
        else:
            print(message())
            sleep(2)
            os.system('cls')
            return tablet()
        # right hand path
    elif response1 == "2":
        os.system('cls')    
        print("You get blocked by a boulder")
        print("   ")
        return boulder_push()

    # Attempt to climb directly up
    elif response1 == "3":
        os.system('cls')
        print("\nAn avalanche falls on you.")
        print("   ")
        print("You die!!!")
        print("   ")
        return act_3_death()

    else:
        os.system('cls')
        print(message())
        sleep(2)
        return tablet()

def boulder_push():
    global time_left
    response3 = input("Do you push the boulder off the edge? [Y]/[N]: ")            
    if response3.lower() == "y" or response3.lower() == "yes":
        time_left -= 3
        print("\nYou hear the screams of something getting crushed below")
        print("   ") 
        print("You continue up the mountain")
        print("   ")
        sleep(3)
        os.system('cls')   
        return snow_section()
    elif response3.lower() == "n" or response3.lower() == "no":
        print("\nThe boulder gives way and crushes you anyway")
        print("   ") 
        print("You die!!!")
        print("   ")   
        return boulder_death()
    else:
        print(message()) 
        return tablet()

def boulder_death():
    global time_left
    res = input("Would you like to [A] make that decision again or [B] start again?: ")
    if res.lower() == "a":
        time_left -= 3
        sleep(2)
        os.system('cls')
        print(f"{time_left} hours remaining")
        print(time_remaining())
        return boulder_push()
    elif res.lower() == "b":
        time_left = 24
        return start()
    else:
        print(message())
        return boulder_death()

def act_3_death():
    global time_left
    res = input("Would you like to [A] make that decision again or [B] start again?: ")
    if res.lower() == "a":
        time_left -= 3
        sleep(2)
        os.system('cls')
        print(f"{time_left} hours remaining")
        print(time_remaining())
        return tablet()
    elif res.lower() == "b":
        time_left = 24
        return start()
    else:
        print(message())
        return act_3_death()

def snow_section():
    print(f"{time_left} hours remaining")
    print(time_remaining())

    print("""
    ^**--- Act 4 ---**^

    You shuffle through the increasing flurry of snow,
    until you see a blaring yellow light emerging from a cave like opening.

    "There's the entrance to your destiny" Mercearius exclaimes.
    You nod your head in agreement, and stroll in without haste.
    ​
    You survived the extremeties on The Forsaken Summit. You're good at this! ;)
    Mercearius utters a bizzare chirp of glee

    Inside the Ancient ruins of the Vault of spirits,
    you are met by Gamek the keeper of the Vaults

    "Don't be alarmed", Mercearius acknowledges you are frightened.
    "This one looks just as awful as the other creatures, but he will be fair"
    You blurt out a cry of uncertainty.

    "I don't know of this beast, or the contents of this ruin."
    "I don't remember reading about any of this in the forbidden books".

    Gamek the keeper, turns and points to the middle of the room.
    There stands a magnificant purple rune, glimmering with light. 
    It seemed to be connected to three smaller runes around the perimiter, attached by some unknown force.

    "There is only one" you hear a whispering voice in the muggy air.
    Mercearius shifts round to your head.
    "Forget all this weirdness, and just pick one of the runes. Your guess is as good as mine"
    ​
    You gulp, and walk into the middle of the fantastical structure.
    "Just listen to your intuition and pick a rune, said Mercearius.
    \n\033[1;34;40m Mercearius' blue aura guide your eyes to a stone tablet in front of you, with three choices\033[0;37;40m\n""")

    return pick_rune()

# Rune decision
def pick_rune():
    res = input("\nWhich rune will you pick? [A] Yellow, [B] Red or [C] Orange?: ")
    os.system('cls')
    if res.lower() == "a":
        print("""\n You used the Obra Rune                                                                                                                                                

        A yellow beam of light hits you - you explode! DEATH!\n""")                                                                   
        
        
        return rune_death()                                                     
    elif res.lower() == "b":
        os.system('cls')
        print("""You used the Terth Rune

        A red beam of light hits you - a strong energy fills your body and mind.

        You burst upwards and break through the ruin, gliding further and further up

        With a sudden flash of light...""")

        sleep(5)
        os.system('cls')

        rune_b_2 = """

     .edee...      .....       .eeec.   ..eee..
   .d*"  """"*e..d*"""""**e..e*""  "*c.d""  ""*e.
  z"           "$          $""       *F         **e.
 z"             "c        d"          *.           "$.
.F                        "            "            'F
d                                                   J%
3         .                                        e"
4r       e"              .                        d"
 $     .d"     .        .F             z ..zeeeeed"
 "*beeeP"      P        d      e.      $**""    "
     "*b.     Jbc.     z*%\e.. .$**eeeeP"
        "*beee* "$$eeed"  ^$$$""    "
                 '$$.     .$$$c
                  "$$.   e$$*$$c
                   "$$..$$P" '$$r
                    "$$$$"    "$$.           .d
        z.          .$$$"      "$$.        .dP"
        ^*e        e$$"         "$$.     .e$"
          *b.    .$$P"           "$$.   z$"
           "$c  e$$"              "$$.z$*"
            ^*e$$P"                "$$$"
              *$$                   "$$r
              '$$F                 .$$P
               $$$                z$$"
               4$$               d$$b.
               .$$%            .$$*"*$$e.
            e$$$*"            z$$"    "*$$e.
           4$$"              d$P"        "*$$e.
           $P              .d$$$c           "*$$e..
          d$"             z$$" *$b.            "*$L
         4$"             e$P"   "*$c            ^$$
         $"            .d$"       "$$.           ^$r
        dP            z$$"         ^*$e.          "b
       4$            e$P             "$$           "
                    J$F               $$
                    $$               .$F
                   4$"               $P"
                   $"               dP"""
        
        print(rune_b_2)   

        sleep(2)
        os.system('cls')

        print("""
        ZAP!!! -
        
        you mysteriously appear at the gates of the Kingdom of Sterus.

        With your crown and robes back on your body, it's time to take your Kingdom back.""")

        sleep(5)
        os.system('cls')
        
        return end_story()
    elif res.lower() == "c":
        os.system('cls')
        print("""You used the Holl Rune

        An orange beam of light hits you and you disintegrate - DEATH!\n""")
        
        return rune_death()
    # If an unexpected input is detected
    else:
        print(message())
        return pick_rune()
    
def rune_death():
    global time_left
    res = input("Would you like to [A] try a different rune? or [B] Start again?: ")
    if res.lower() == "a":
        time_left -= 2
        sleep(2)
        os.system('cls')
        print(f"{time_left} hours remaining")
        print(time_remaining())
        return pick_rune()
    elif res.lower() == "b":
        sleep(2)
        os.system('cls')
        time_left = 24
        return start()
    # If an unexpected input is detected
    else:
        print(message())
        return rune_death()


def end_story():

    ending = f"""\n 
    
    You survived with {time_left} hours remaining!"""
     
    ending_1 = f"""
                                 _         _       _   _                 
  ___ ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___ 
 / __/ _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
| (_| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \\
 \___\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                 |___/                                                   
​
​The High Leader confidently strolled throught the gates of his Kingdom. The guards and towns-people gasped in disbelef and dropped to their knees. They had given up hope.
By now the Kingdom looked unrecognisable. Crops weren't growing, and the residents looked tired and over-worked. Houses looked shabby and paths were neglected. There was
even a new graveyard for the recently deceased.

"Too soon" the High Leader muttered under his breath, as he saw the graves of young adults. "What's been happening here"? He bellowed.

As he looked up the castle path, he caught a glimpse of the the culprits who banished him.

"If only I had the power to blast these traitors away like they did to me" he thought.

At that moment, he notices a shine in his pocket. It's the very rune that transported him out from the Overworld.

A faint whisper caught his ear in the wind. "Use the rune to do to them what they did to you. You have that power now!" It was the sweet voice of Mercearius.

The High Leader smirked, waltzed up to the castle, kicked the door through, and with a epic ray of light from the rune, BOOOM!!! Within a flash, the hand of the High Leader and the Sorceror were gone.

Peace and prosperity would be restored once again.
​
The end...\n"""

    print(ending)
    print(time_remaining())
    print(ending_1)
    sleep(2)

    return play_again()

def play_again():
    res = input("Would you like to play again? [Y]/[N]: ")
    if res.lower() == "y":
        os.system('cls')
        return start()
    elif res.lower() == "n":
        os.system('cls')
        print("Thanks for playing!")
    else:
        print(message())
        res = input("\nWould you like to play again? [Y]/[N]: ")
        if res.lower() == "y":
            os.system('cls')
            return start()    
        elif res.lower() == "n":
            os.system('cls')
            print("Thanks and goodbye... ")
            print("If you want to offer any of our team a job as a junior developer then we probably won't say no!")
            print("What else would we be doing???")
            print("Ask Code Nation for our details! ;) ")
        else:
            return time_remaining()  

def time_remaining():
    if time_left > 18:
        return time_1
    elif time_left > 12:
        return time_2
    elif time_left > 6:
        return time_3
    elif time_left > 0:
        return time_4
    else:
        print(time_1)
        print(time_runs_out)
        res = input("\nWould you like to play again? [Y]/[N]: ")
        if res.lower() == "y":
            os.system('cls')
            return start()    
        elif res.lower() == "n":
            os.system('cls')
            print("Thanks and goodbye... ")
            print("If you want to offer any of our team a job as a junior developer then we probably won't say no!")
            print("What else would we be doing???")
            print("Ask Code Nation for our details! ;) ")
        else:
            return time_remaining()    

def message():
    list_of_messages = [
        "\nSorry, I didn't understand that.\n",
        "\nChoose again please!\n",
        "\nEnough with your inconsistent ramblings you vagabond!\n",
        "\nSay what????????\n",
        "\nThat definitely didn't make any sense.\n"
    ]
    return choice(list_of_messages)

start()

pygame.mixer.music.stop()
pygame.mixer.quit()