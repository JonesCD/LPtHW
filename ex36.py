from sys import exit

def tire_store():
	print "\n\n\n\n\nYou are in front of the tire shop."
	print "The light is red to cross 4th Ave."
	print "A car is blocking the handicapped ramp to cross Butler."
	print "Do you wait for the light, or try to get around the car?"
	
	while True:
		choice = raw_input("\n\n> ")
		
		if "wait" in choice:
			print "\n\n\n\n\nGood. Safety first!"
			bandana_man()
		elif "around" in choice:
			late("A car swerved and crashed into the stroller! \nNow you have to go back for the Bjorn, and will be late to pickup! \nHaste makes waste!")
		else:
			print "I don't understand. Will you 'wait' or 'go around'?"
			
def bandana_man():
	print "You are now passing Sheep Station."
	print "That fellow with a million bandanas sticking out of his clothes, \nis hanging around, as usual."
	print "You've always been curious - what's the deal with the bandanas?"
	print "Do you ask him about it? yes or no"
	
	choice = raw_input("\n\n> ")
	if choice == "yes":
		late("He's clearly crazy. He won't stop talking. \nSomething about colors. \nYou can't get away, and are late to pickup!")
	elif choice == "no":
		print "\n\n\n\n\nGood choice. Now's not the time to engage. \nYou're running late, after all!"
		coned_truck()
	else:
		late("That's not y or n. \nDid you stop for a few glasses of Australian wine or something. \nYou've missed pickup!")
		
def coned_truck():
	print "We're only a half block from Daddy's Daycare!"
	print "There's a ConEd truck, and a bunch of workers rushing. \n...Almost in a panic."
	print "It smells vaugly of gas."
	print "Do you turn back and go around the block up Degraw for safety?"
	print "Type 'charge on' or 'go around'"
	
	while True:
		choice = raw_input("\n\n> ")
	
		if choice == "charge on":
			print "\n\n\n\n\nGood choice. These workers are professionals, after all."
			print "You don't have the baby yet, and surely daycare \nwill forgive lateness if they hear you explode."
			print "Of course, you'll walk home around the block for safety."
			daddys_queue()
		elif choice == "go around":
			late("You don't have \n\t1) time for that, \n\t2) the baby yet, so she's safe, and \n\t3) trust in these professionals! You're late to pickup!")
		else:
			print "Typo much, Monkey fingers?"
			
def daddys_queue():
	print "You've made it to daycare, in the nick of time!"
	print "But, there's a long queue. Oh no!"
	print "Do you wait patiently, or..."
	print "do you push ahead to make sure you officially pick up before 6p?"
	
	while True:
		choice = raw_input("\n\n> ")
		
		if "wait" in choice:
			print "\n\n\n\n\nYou were there on time, and got the Nut just a few minutes after 6!"
			print "They don't charge for that!"
			print "Have fun walking and playing with the baby!"
			exit(0)
		elif "push" in choice:
			print "Kinda jerky."
			print "The other parents don't like you much now."
			print "And the ladies at daycare think you're rude."
			late("Now you get late charges in 10 second increments!")
		else:
			print "What are you doing? Type 'wait' or 'push ahead'. There's no other choice for a line!"

def late(result):
	print result, "Boo!"
	exit(0)
	
def start():
	print "You got out of work late!"
	print "You have no time to spare to get the baby before 6p!"
	print "You've grabbed the stroller, and can rush off."
	print "Do you have everything else you need? \nIf you're ready to go, type yes"
	
	choice = raw_input("\n\n> ")
	
	if choice == "yes":
		tire_store()
	else:
		late("Might as well go do some emails then.	\nYou're late, and it's going to cost you!")
		
start()