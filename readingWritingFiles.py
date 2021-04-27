'''
Lab Instructions

Create a program that accepts user input and allows you to add places to a text file that you'd like to travel to. The program should:

    Create the file and call it travel-bucket-list.txt if it doesn't already exist.
    Ask you Where would you like to travel? as a user prompt.
    Add the answer you give it to the list you've saved in your text file.
    Say Great, I've added to your list! Anywhere else? and offer you an input to add more.
    Allow you to quit the program if you type the word quit and say Ok, goodbye! when it quits.
'''

import sys

print('Where would you like to travel?')

while True:
	user_input = input('Name of place: ')
	if user_input == 'q':
		print('Ok, goodbye!')
		break
	elif user_input != 'q':
		with open('file.txt', 'a+') as file:
			file.write(user_input + '\n')
			print('\n' + 'Great, I\'ve added to your list! Anywhere else?')
			print("Enter 'q' if you're done adding to your list.")
