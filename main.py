from art import logo, vs
from game_data import streamers
from random import randint
from os import system

lost = False
streamers_temp = streamers.copy()
score = 0


def clear():
    _ = system('clear')


def get_streamer():
    global streamers_temp
    streamer = list(streamers_temp.items())[randint(0, len(streamers_temp) - 1)]
    streamers_temp.pop(streamer[0])
    return streamer


streamer1 = get_streamer()

print(logo)
while not lost and streamers_temp:
    next_streamer = get_streamer()
    follower_count1 = "{:,}".format(streamer1[1])
    print(f'Compare A: {streamer1[0]}, {follower_count1}')
    print(vs)
    print(f'Compare B: {next_streamer[0]}')
    choice = input("Who has more subs? Type 'A' or 'B': ").upper()
    follower_count2 = "{:,}".format(next_streamer[1])
    if choice == 'A':
        if streamer1[1] > next_streamer[1]:
            score += 1
            clear()
            print(logo)
            print(f'You are right! {streamer1[0]} has {follower_count1} subs and '
                  f'{next_streamer[0]} has {follower_count2} subs')
            print(f' Current score: {score}')
        else:
            print(f'Sorry that is wrong, {streamer1[0]} has {follower_count1} subs and '
                  f'{next_streamer[0]} has {follower_count2} subs')
            print(f'final score: {score}')
            lost = True
    else:
        if streamer1[1] < next_streamer[1]:
            streamer1 = next_streamer
            score += 1
            clear()
            print(logo)
            print(f'You are right! {streamer1[0]} has {follower_count1} subs and '
                  f'{next_streamer[0]} has {follower_count2} subs')
            print(f' Current score: {score}')
        else:
            print(f'Sorry that is wrong, {streamer1[0]} has {follower_count1} subs and '
                  f'{next_streamer[0]} has {follower_count2} subs')
            print(f'final score: {score}')
            lost = True

if not streamers_temp:
    print('YOU COMPLETED THE GAME !!!')
