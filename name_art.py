from pyfiglet import Figlet
import random

figlet = Figlet()
figfonts = figlet.getFonts()

def name_gen():
    while True:
    	random.seed()
    	figlet.setFont(font=random.choice(figfonts))
    	print(figlet.renderText('Name Generator'))
    	name = input('What name would you like?: ')
    	print('Welcome to the Name Generator!')
    	print('This program will generate a random ascii art with your name for you.')
    	print(figlet.renderText(f'{name}'))
    	rep = input('Exit: ')
    	if rep == 'yes':
        	print(figlet.renderText('GAME OVER !!'))
        	break
name_gen()
