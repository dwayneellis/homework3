# CIS 2348 Homework 3 Fall 2020.
# Dwayne Ellis
# Student ID: #######
# Lab 11.27 Soccer team roster (Dictionaries)
# This program will store roster and rating information for a soccer team. Coaches rate players
# during tryouts to ensure a balanced team.

# Prompt user to input 5 pairs of numbers
team = {}

i = 1

count = 1

for i in range(1, 6):

    jersey = int(input('Enter player {}\'s jersey number:\n' .format(i)))

    rating = int(input('Enter player {}\'s rating:\n\n' .format(i)))

    if jersey < 0 and jersey > 99 and rating < 0 and rating > 9:

        print('invalid entry')

        break

    else:

        team[jersey] = rating

print("ROSTER")

for jersey, rating in sorted(team.items()):

    print("Jersey number: %d, Rating: %d" % (jersey, rating))

menu_option = ''

# Loop until user quits

while menu_option.upper() != 'Q':

    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr'
          ' - Output players above a rating\no - Output roster\nq - Quit\n')

    menu_option = input('Choose an option:\n')

    if menu_option == 'a':

        jersey = int(input('Enter a new player\'s jersey number:\n' .format(i)))

        rating = int(input('Enter the players\'s rating:' .format(i)))

        team[jersey] = rating

    elif menu_option == 'd':

        jersey = int(input('Enter a jersey number:'))

        if jersey in team.keys():

            del team[jersey]

    elif menu_option == 'u':

        jersey = int(input('Enter a jersey number: '))

        if jersey in team.keys():

            rating = int(input('Enter a new rating for player: '))

            team[jersey] = rating

    elif menu_option == 'r':

        # get  rating

        rating_input = int(input('Enter a rating'))

        print('ABOVE {}'.format(rating_input))

        # print all players with rating above defined rating

        for jersey, rating in sorted(team.items()):

            if rating > rating_input:

                print("Jersey number: %d, Rating: %d" % (jersey, rating))

    elif menu_option == 'o':

        # print the soccer team's Roster

        print("ROSTER")

        for jersey, rating in sorted(team.items()):

            print("Jersey number: %d, Rating: %d" % (jersey, rating))
