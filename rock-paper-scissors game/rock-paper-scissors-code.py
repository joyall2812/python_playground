import random
print("hellooo ☺")
user_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']
a = input('do you want to play rock-paper-scissors with me? (y/n): ')
if a == 'y':
    b = int(input("enter the max score:"))
    while user_score < b and computer_score < b:
        user_pick = input('enter rock/paper/scissors:').lower()
        if user_pick not in choices:
            print('thats illegal 🚓')
            continue
        random_number = random.randint(0, 2)
        computer_pick = choices[random_number]
        print(f'computer picked : {computer_pick}')
        if user_pick == 'rock' and computer_pick == 'scissors':
            user_score += 1
            print('you won this round we will see next🤺 ')
        elif user_pick == 'scissors' and computer_pick == 'paper':
            user_score += 1
            print('you won this round we will see next🤺 ')
        elif user_pick == 'paper' and computer_pick == 'rock':
            user_score += 1
            print('you won this round we will see next🤺')
        elif user_pick == computer_pick:
            print("thats a draw 🤝")
            continue
        else:
            computer_score += 1
            print('haha i scored 😎')

    if computer_score == b:
        print('haha i won 😎')
        print(f'my score is {computer_score} of course😎')
        print(f'your score is {user_score}🥱')
    else:
        print('you won 🙄🙄🙄')
        print(f'your score is {user_score} of course🥱')
        print(f'my score is {computer_score}😪')
    print('hehe good game 😊')
