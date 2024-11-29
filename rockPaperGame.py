import random


user_score=0
computer_score=0


while True:
    user_choice=input("chose rock/paper/scissor or q to quit: ").lower()
    computer_choice=["rock","paper",'scissor']
    computer=random.randint(0,2)

    if user_choice=="q":
        break
    else:

        if user_choice not in computer_choice:
            continue
        if user_choice == computer_choice[computer]:
            print("matched")
            continue
        if user_choice != computer_choice :
            if user_choice =="rock" and computer_choice[computer] == "paper":
                print("computer wins")
                computer_score +=1
            
            elif user_choice =="paper" and computer_choice[computer] == "rock":
                print("user wins")
                user_score +=1
            if user_choice =="paper" and computer_choice[computer] == "scissor":
                print("computer wins")
                computer_score +=1
            
            elif user_choice =="scissor" and computer_choice[computer] == "paper":
                print("user wins")
                user_score +=1
            if user_choice =="rock" and computer_choice[computer] == "scissor":
                print("computer wins")
                computer_score +=1
            
            elif user_choice =="scissor" and computer_choice[computer] == "rock":
                print("user wins")
                user_score +=1
            
            
        


print(f"user:{user_score}\ncomputer:{computer_score}")