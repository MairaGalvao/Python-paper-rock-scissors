import time
print ("Lets play a fun game!")
time.sleep(2)
User1 = str(input("User 1: Whats your name?"))
User2 = str(input("User 2: Whats your name?"))

bet1 = str(input (User1 + ", pick between 'rock', 'paper' or scissors' ?"))
bet2 = str (input(User2 + ", pick between 'rock', 'paper' or scissors' ?"))

def game (user1_answer, user2_answer):

    if user1_answer == ("rock") and user2_answer == ("rock"):
        print("No winner this time! Let's play it again?")
    elif user1_answer == ("rock") and user2_answer == ("paper"):
            print (User2 + " , congrats, you are the winner")
    elif user1_answer == ("rock") and user2_answer == ("scissors"):
            print (User1 + ", you rock at playing this game!! Congratulations")
    elif user1_answer == ("paper") and user2_answer == ("rock"):
            print (User1 + ", you are the winner")
    elif user1_answer == ("paper") and user2_answer == ("paper"):
            print ("Tie! Try it again")
    elif user1_answer == ("paper") and user2_answer == ("scissors"):
            print (User2 + ", so exciting, you won! ")
    elif user1_answer == ("scissors") and user2_answer == ("rock"):
            print (User2 + ", you are the winner")
    elif user1_answer == ("scissors") and user2_answer == ("paper"):
            print (User1 + ", thats amazing, you are the winner")
    elif user1_answer == ("scissors") and user2_answer == ("scissors"):
            print ("nobody won this time.")
    else:
            print ("It seems that you did not type a valid answer, please try again.")
game (bet1, bet2)

print("Super fun, right?")
time.sleep(2)
print("Would you like to play it again?")
Answer = str(input())
if Answer == ("yes"):
    print("Cool, so lets do it!")
else:
    print("Oh, okay, see you next time")