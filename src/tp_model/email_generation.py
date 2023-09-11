
import random

def return_random_message(messages):
      return random.choice(messages)

def driver_retirement(driver):
	retirement_messages = [
	f"{driver.name} has announced his retirement from racing at the age of {driver.age}.",
		f"After a long and successful career, {driver.name} has decided to retire at the age of {driver.age}.",
		f"{driver.name} is hanging up his helmet at the age of {driver.age}. Retirement beckons!",
		f"At {driver.age} years old, {driver.name} has decided to call it a day on their racing career.",
    ]

    # Choose a random retirement message from the list
	selected_message = random.choice(retirement_messages)
    
	return selected_message

def driver_hiring_email(team, driver):
    hiring_messages = [
        f"{driver.name} has joined forces with {team.name} for the next season. Together, we aim for victory!",
        f"{team.name} is proud to announce the signing of {driver.name} as our new driver.",
        f"{team.name} is excited to welcome {driver.name} to our racing family.",
        f"{driver.name} joins the ranks of {team.name} as our newest driver. Let's achieve greatness together!",
    ]

    # Choose a random hiring message from the list
    selected_message = random.choice(hiring_messages)
    
    return selected_message

def upgrade_facility(team, facility):
	messages = [
		f"Exciting news! {team.name} has completed an upgrade to their {facility}.",
		f"{team.name} is investing in excellence with the latest upgrade to their {facility}.",
		f"Attention all fans! {team.name} has improved their {facility} to enhance performance.",
		f"Breaking news: {team.name} unveils an upgraded {facility} to stay at the forefront of F1 technology.",  
		]
    
	return return_random_message(messages)

def hire_technical_director_email(team, technical_director):
	messages = [
		f"Big news! {team.name} welcomes {technical_director.name} as our new Technical Director.",
		f"{technical_director.name} joins the ranks of {team.name} as the Technical Director, ready to lead us to success.",
		f"{team.name} is thrilled to announce the appointment of {technical_director.name} as our new Technical Director.",
		f"Get ready for a new era at {team.name} with {technical_director.name} taking the helm as Technical Director.",
    ]

	return return_random_message(messages)