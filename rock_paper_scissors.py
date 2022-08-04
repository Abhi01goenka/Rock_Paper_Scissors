import time
import os
import random

def win(s1, s2):
    if(s1 == 'rock'):
        if(s2 == 'rock'):
            return 'Tie'
        elif(s2 == 'paper'):
            return '2'
        elif(s2 == 'scissors'):
            return '1'
    elif(s1 == 'paper'):
        if(s2 == 'rock'):
            return '1'
        elif(s2 == 'paper'):
            return 'Tie'
        elif(s2 == 'scissors'):
            return '2'
    elif(s1 == 'scissors'):
        if(s2 == 'rock'):
            return '2'
        elif(s2 == 'paper'):
            return '1'
        elif(s2 == 'scissors'):
            return 'Tie'


os.system("cls")
print("Rock, Paper and Scissors!!\n\n\n")
no_of_rounds = int(input("Enter number of rounds : "))
max_points = int(input("Enter maximum points : "))
user_rounds = 0
computer_rounds = 0
round = 0
l = ['rock', 'paper', 'scissors']
os.system("cls")
while(no_of_rounds):
    round += 1
    print("Round ", str(round))
    print("\n\n")
    no_of_rounds -= 1
    user_points = 0
    computer_points = 0
    while(user_points != max_points and computer_points != max_points):
        ch = input("Enter your choice : ").lower() 
        r = random.randrange(0, 3)
        print("User's choice     :", ch)
        print("Computer's choice :", l[r])
        w = win(ch, l[r])
        if(w == '1'):
            print(ch, "beats", l[r])
            user_points += 1
        elif(w == '2'):
            print(l[r], "beats", ch)
            computer_points += 1
        else:
            print("Tie")
        print(user_points,computer_points)
        print("\n\n")
        time.sleep(1)
    if(user_points == max_points):
        print("User wins Round", str(round))
        user_rounds += 1
    elif(computer_points == max_points):
        print("Computer wins Round", str(round))
        computer_rounds += 1
    time.sleep(2)
    os.system("cls")

print("Number of rounds won by User     : ", str(user_rounds))
print("Number of rounds won by Computer : ", str(computer_rounds))
if(user_rounds > computer_rounds):
    print("User wins!!")
elif(computer_rounds > user_rounds):
    print("Computer wins!!")
else:
    print("There is a Tie!!")
