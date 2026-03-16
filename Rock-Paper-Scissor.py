import random

again = "y"

while again == "y":
    lst = ['rock', 'paper', 'scissor']

    com_list = random.choice(lst)
    # print(com_list)

    user_lst = input("Enter Your Choice: ")

    if com_list == user_lst.lower:
        print("You Both Guess same Then Game is Tie!")
    elif com_list == 'rock' and user_lst.lower == 'paper':
        print("User Win! ")
    elif com_list == 'scissor' and user_lst.lower == 'rock':
        print("User win! ")
    elif com_list == 'paper' and user_lst.lower == 'scissor':
        print("User Win!")
    else:
        print("Computer Win!")
    again = input("Do You Want To Run Again (y/n): ")
print("You Exit From Program! ")



