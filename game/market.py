import os
import sys
import time
#list , consumable items ONLY: Lv1-3 Potions, Revives, common ingredients food&alchemy
potions = ["Potion", "Super Potion", "Revive", "Antidote"]
food = ["Bread", "Cheese", "Raw Meat"]
alchemy = ["Dragonfly Tail", "Butterfly Wings", "Salt", "Troll Blood"]

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")
#def give_gold()
	
clear_screen()	
print("Hello, how can I help you?  ")
print("We sell healing items, food and some alchemy ingredients.")
order = input("What would you like?  ")
if order.lower() == 'healing items' or 'potions' or 'healing':
	print("Alright, we have ", potions)
if order.lower() == 'food':
	print("Ok, we have ", food)
if order.lower() == 'alchemy' or 'ingredients' or 'alchemy ingredients':
	print("Sure, we have ", alchemy)
