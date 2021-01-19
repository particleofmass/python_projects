from random import choice
from time import sleep, process_time, time 
import os

superset = [str(i) for i in range(2,11)] + 'Ace King Queen Jack'.split()
suits = 'Clubs Diamonds Hearts Spades'.split()
check_list = []
attempt_list = []

level = int(input('Enter difficulty level :'))

for i in range(level):
    os.system('clear')
    rank, suit = choice(superset), choice(suits)
    check_list.append([rank, suit])
    print(rank, ' of ', suit)
    sleep(1)

yes = 'y ye yes yeah yup yip yo yea'.split()
attempt = 'no'
os.system('clear')
print('                                     \n\n\n\n\n\n\n\n\n                 Get ready for the test!')
sleep(2)
os.system('clear')
while attempt.strip().lower() not in yes: 
    attempt = input('\n\n\n\n\n\nType yes when ready for the test :  ')

if attempt.strip().lower() in yes:
    for i in range(level):
        os.system('clear')
        print('\n\n\nCard number ',i+1)
        ans_rank = input('\nEnter the rank for the card  \n  (eg - 1 or 10 or j - for jack) : ')
        ans_suit = input('\nEnter the suit for the card \n (ex - c for clubs, s for spades,etc.) : ')
        if ans_suit.lower() == 'c':
            ans_suit = 'Clubs'
        elif ans_suit.lower() == 's':
            ans_suit = 'Spades'
        elif ans_suit.lower() == 'h':
            ans_suit = 'Hearts'
        elif ans_suit.lower() == 'd':
            ans_suit = 'Diamonds'
        attempt_list.append([ans_rank, ans_suit])

os.system('clear')
if check_list == attempt_list:
    print('\n\n\n\n\n\n                     You won  !!!!!!!!!!!!!')
elif check_list != attempt_list:
    print('\n\n\n\n\n\n                         Loser...')
print(f'\n\n\n\n\nThe real sequence was          :    {check_list}\n\nThe sequence you submitted was :     {attempt_list}\n\n\n')
