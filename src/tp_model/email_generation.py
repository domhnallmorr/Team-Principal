
import random

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