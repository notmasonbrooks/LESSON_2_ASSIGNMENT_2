# task 1 code correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"

if attendees >= 50:
    action = input("Would you like to add a projector? (yes/no)")
    if action == "yes":
        print("sounds good.")
    else:
        print("no worries.")
elif attendees >= 200:
    action = input("Would you like to add a sound system? (yes/no)")
    if action == "yes":
        print("good choice.")
    else:
        print("no worries.")
action = input("Would you like vegetarian catering? (yes/no)")
if action == "yes":
    print("We recommend Veggie Delight Catering")
else: 
    print("Gourmet Meals Catering")

print(f"We recommend you to book our {venue}")