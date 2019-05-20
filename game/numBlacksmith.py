import os
import sys
import time


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


clear_screen()
print("Type '1' for option 1")
print("Type '2' for option 2")
print("Type '3' for option 3")
print("Type '4' for option 4")
print("""


""")
clear_screen()
print("You see a man hammering away at a war Axe by the forge, the Blacksmith.")
approach = input("""Do you approach?  <YES> <NO> """)
if approach.lower() == 'no' or '2':
	print("You turn away from the blacksmith.")
	print("You head back to the town center.")
	sys.exit
if approach.lower() == 'yes' or '1':
	print("You approach the Blacksmith.")
	print("He has yet to notice you.")
	attention = input("Grab his attention?  ")
	if attention.lower() == 'yes':
		print("You announce your presence and ask how much for a new weapon.")
		print("...")
		print("He doesn't respond.")
		pester = input("Ask him again?  ")
		if pester.lower() == 'yes':
			print("You start to repeat yourself but as you begin to speak he cuts you off.")
			print("'I heard ya the first time.' He speaks in a deep, thick northern accent. 'Come pester me when you're important enough to interrupt ma work'")
			print("He waves his hand for you to leave.")
		if pester.lower() == 'no':
			print("He seems busy. Maybe I should leave.")
			leave = input("Leave?  ")
			if leave.lower == 'yes':
				print("You head back to the town center")
				if leave.lower == 'no':
					print("You stand around for a few minutes.")			
	if attention.lower() == 'no':
		print("You patiently wait for him to finish his work.")
		print("Still hammering away at the weapon he glances up at you.")
		print("'Whaddya want?' He speaks in a deep, thick northern accent. 'Can't ya see I'm in the middle of somethin'?'")
		services = input("Ask him for a new weapon?  ")
		if services.lower() == 'yes':
			print("You ask the Blacksmith for a superior weapon, one that'll last you long and serve you well.")
			print("The Blacksmith halts his hammering to look at you.")
			print("'Who the hell do ya think you are?'")
			print("'You want a weapon, lad? Go to the guild and buy yourself a piece. I ain't got time for the likes of yous'.")
			print("The Blacksmith waves you off and continues his work.")
		if services.lower() == 'no':
			print("...")
			print("The Blacksmith puts down his repair hammer and starts to grip the handle of the war Axe.")
			print("The Blacksmith howls 'Then what the fuck you doing here then?'")
			print("You start to back off and head back to the town center.") 		
print("Maybe you can get a weapon elsewhere.")		
print("End")
