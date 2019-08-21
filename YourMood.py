#YourMood
#Ted Yarmoski

#Note: I use "mood" and "feeling" interchangeably in my comments

import os

#Additional moods should be added here first
feelings = ['happy', 'sad', 'calm', 'angry']
#These should be only desirable moods
target_feelings = ['happy', 'calm']





while True:
	feeling = input('How are you feeling?\n')
	#If user inputs valid feeling
	if feeling.lower() in feelings:

		#Depending on mood entered, print appropriate strings
		if feeling.lower() in ['happy']:
			print("\nThat's great!")
			#Takes user input for suggestion, creates file if it does not exist
			happy_input_suggestion = input('\nWhat you were doing, or how did you achieve this feeling?\n')
			with open("happy_suggestions.txt","a") as hs:
				hs.write(happy_input_suggestion + "\n")
			#If reminders have been made before, access
			if os.path.isfile('./happy_reminders.txt'):
				print("\n\nHere are your past reminders:")
				with open("happy_reminders.txt","r") as hr:
					print(hr.read())
			else:
				print("You don't have any past reminders.")
			#Takes user input for reminder, creates file if it does not exist
			happy_input_reminder = input('\nRemind yourself of something when you are happy again:\n')
			with open("happy_reminders.txt","a") as hr:
				hr.write(happy_input_reminder + "\n")

		#Other feelings are similar to the "happy" one, comments ommitted
		elif feeling.lower() in ['calm']:
			calm_input_suggestion = input('\nWhat you were doing, or how did you achieve this feeling?\n')
			with open("calm_suggestions.txt","a") as hs:
				hs.write(calm_input_suggestion + "\n")
			if os.path.isfile('./calm_reminders.txt'):
				print("\n\nHere are your past reminders:")
				with open("calm_reminders.txt","r") as hr:
					print(hr.read())
			else:
				print("You don't have any past reminders.")
			calm_input_reminder = input('\nRemind yourself of something when you are calm again:\n')
			with open("calm_reminders.txt","a") as hr:
				hr.write(calm_input_reminder + "\n")

		elif feeling.lower() in ['sad']:
			if os.path.isfile('./sad_reminders.txt'):
				print("\n\nHere are your past reminders:")
				with open("sad_reminders.txt","r") as hr:
					print(hr.read())
			else:
				print("You don't have any past reminders.")
			sad_input_reminder = input('\nRemind yourself of something when you are sad again:\n')
			with open("sad_reminders.txt","a") as hr:
				hr.write(sad_input_reminder + "\n")
			print("Here is a helpful resource: https://www.verywellmind.com/sadness-is-not-depression-2330492")
			print("Here is a helpful resource: https://www.samhsa.gov/find-help/national-helpline")

		elif feeling.lower() in ['angry']:
			if os.path.isfile('./angry_reminders.txt'):
				print("\n\nHere are your past reminders:")
				with open("angry_reminders.txt","r") as hr:
					print(hr.read())
			else:
				print("You don't have any past reminders.")
			angry_input_reminder = input('\nRemind yourself of something when you are angry again:\n')
			with open("angry_reminders.txt","a") as hr:
				hr.write(angry_input_reminder + "\n")
			print("Here is a helpful resource: https://www.healthline.com/health/why-am-i-so-angry")
		break
	else:
		print('\nPlease enter a valid choice. (happy, sad, calm, angry)')

target_yn = input('\nDo you want to feel differently than you do now?\n')
if target_yn.lower() in ['yes', 'yea', 'ye', 'y', 'ok', 'yes ']:
	
	while True:
		target = input('\nHow would you like to be feeling right now?\n')
		if target.lower() in target_feelings:
			
				#Displays user suggestions that correspond with the selected target mood if they exist
				if target.lower() == 'happy':
					if os.path.isfile("./happy_suggestions.txt"):
						with open("happy_suggestions.txt","r") as hs:
							print("\n\nHere are your past suggestions to be happy:\n")
							print(hs.read())
							input("\nPress enter to continue...\n")
					else:
						print("You don't have any past suggestions.")
						print("Here is a helpful resource: https://bit.ly/2GZZv3f")
					break 


			
				elif target.lower() == 'calm':
					if os.path.isfile("./calm_suggestions.txt"):
						with open("calm_suggestions.txt","r") as hs:
							print("\n\nHere are your past suggestions to be calm:\n")
							print(hs.read())
							input("\nPress enter to continue...\n")
					else:
						print("You don't have any past suggestions.")
						print("Here is a helpful resource: https://www.healthline.com/health/how-to-calm-down")
					break 

			   
		else:
			print('\nHm... Are you sure you entered that correctly? Please try again.')
else:
	print("\nAlright, that's fine!")
	print("\nHave an amazing day and stay healthy!")
	print("Goodbye!")
	input("\n\n\n(Press enter to close)")
