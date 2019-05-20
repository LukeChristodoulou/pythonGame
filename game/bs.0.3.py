import os
import sys
import time


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")

	
clear_screen()
print("You see a man hammering away at a war Axe by the forge, the Blacksmith.")
time.sleep(1)
approach = input("Do you approach?  ")
if approach.lower() == 'no':
	print("You turn away from the blacksmith.")
	time.sleep(0.5)
	print("You head back to the town center.")
	sys.exit
if approach.lower() == 'yes':
	time.sleep(0.5)
	print("You approach the Blacksmith.")
	time.sleep(1.5)
	print("He has yet to notice you.")
	time.sleep(1.5)
	attention = input("Grab his attention?  ")
	if attention.lower() == 'yes':
		print("You announce your presence and ask how much for a new weapon.")
		time.sleep(1.5)
		print("...")
		time.sleep(1.5)
		print("He doesn't respond.")
		time.sleep(1.5)
		pester = input("Ask him again?  ")
		if pester.lower() == 'yes':
			print("You start to repeat yourself but as you begin to speak he cuts you off.")
			time.sleep(1)
			print("'I heard ya the first time.' He speaks in a deep, thick northern accent. 'Come pester me when you're important enough to interrupt ma work'")
			time.sleep(4)
			print("He waves his hand for you to leave.")
			time.sleep(0.5)
		if pester.lower() == 'no':
			print("He seems busy. Maybe I should leave.")
			leave = input("Leave?  ")
			if leave.lower == 'yes':
				time.sleep(0.5)
				print("You head back to the town center")
				time.sleep(1)
				if leave.lower == 'no':
					time.sleep(1)
					print("You stand around for a few minutes.")			
	if attention.lower() == 'no':
		print("You patiently wait for him to finish his work.")
		time.sleep(1.5)
		print("Still hammering away at the weapon he glances up at you.")
		time.sleep(2)
		print("'Whaddya want?' He speaks in a deep, thick northern accent. 'Can't ya see I'm in the middle of somethin'?'")
		time.sleep(3)
		services = input("Ask him for a new weapon?  ")
		if services.lower() == 'yes':
			print("You ask the Blacksmith for a superior weapon, one that'll last you long and serve you well.")
			time.sleep(2)
			print("The Blacksmith halts his hammering to look at you.")
			time.sleep(2)
			print("'Who the hell do ya think you are?'")
			time.sleep(2)
			print("'You want a weapon, lad? Go to the guild and buy yourself a piece. I ain't got time for the likes of yous'.")
			time.sleep(3)
			print("The Blacksmith waves you off and continues his work.")
		if services.lower() == 'no':
			time.sleep(2)
			print("...")
			time.sleep(2)
			print("The Blacksmith puts down his repair hammer and starts to grip the handle of the war Axe.")
			time.sleep(3)
			print("The Blacksmith howls 'Then what the fuck you doing here then?'")
			time.sleep(3)
			print("You start to back off and head back to the town center.") 
time.sleep(1)			
print("Maybe you can get a weapon elsewhere.")		
print("End")
