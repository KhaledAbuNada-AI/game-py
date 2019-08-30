import time  # import time to sleep some times
import random  # import random to select random objects

# Configure List Of Objects
Places = ['Desert', 'Tunnel', 'Cave']
Tools = ['knife', 'SticK Light', 'Shaft', 'RPj']
Desert_monsters = ['Phoenix', 'Dragon', 'Dinosaur', 'Gints']
Cave_monsters = ['Mice', 'Snakes', 'wolfes', 'dogs']
Tunnel_monsters = ['Spiders', 'Scorpion', 'Worm', 'Copra']
Game_Reasult = ['alive', 'Died']
Choise = ''


# End Configuration
# Define Function To Print Massages
def PrintSleep(msg, seconds):
    print(msg + '\n')
    time.sleep(seconds)


def start_game():
    PrintSleep('Welcome to the best game for advenures and entertainment', 3)
    PrintSleep('takes you to another world of fiction and amagination', 3)
    PrintSleep('We will help you during the game choices, but you must use your mind before any selection to win ', 2)
    name = input('Please Enter Your Name To Start Game \n')
    time.sleep(2)


def play():
    print('please choose any places that you want to play \n')
    time.sleep(2)
    for place in Places:
        print(place)
        time.sleep(2)
    Choise = ''
    while Choise not in Places:
        Choise = input('Select your choise\n')
        if Choise.lower() == 'Desert'.lower() or Choise.lower() == 'D'.lower() or Choise == '1':
            Choise = 'Desert'
        elif Choise.lower() == 'Cave'.lower() or Choise.lower() == 'C'.lower() or Choise == '2':
            Choise = 'Cave'
        elif Choise.lower() == 'Tunnel'.lower() or Choise.lower() == 'T'.lower() or Choise == '3':
            Choise = 'Tunnel'
        else:
            Choise = ''
            time.sleep(3)


def places():
    print('You have a tool ')
    toolchoosed = random.choice(Tools)
    print(toolchoosed)
    changerequest = input('did you like to change your tool\n')
    if changerequest == 'yes':
        toolchoosed = random.choice(Tools)
        print(toolchoosed)
        print('\nyou now start in ' + Choise + ' and you have a tool ' + toolchoosed)
        time.sleep(3)
        print('Now you face ')
    if Choise == 'Desert':
        print(random.choice(Desert_monsters))
    if Choise == 'Cave':
        print(random.choice(Cave_monsters))
    if Choise == 'Tunnel':
        print(random.choice(Tunnel_monsters))
        time.sleep(3)
        PrintSleep('use the tool to kill the monster before he kill you\n', 3)
        print('you ' + random.choice(Game_Reasult))
        time.sleep(3)
        print('Game Over')


def play_again():
    PA = input("Would you like to play again? (y/n)").lower()
    if PA == "y":
        print("Excellent! Restarting the game ...")
        start_game()
    elif PA == "n":
        print("Thank you for playing!\n" "Good bye!")
    else:
        print("Invaild input")
        breakpoint()

        play_again()

def game():
    start_game()
    play()
    places()


game()