#promting the user to enter their first and last name and bio message
first_name = input("Enter your first name: ").strip()
second_name = input("Enter your second name: ").strip()
bio = input("Enter boi message: ").strip()

#creating the user name
username = first_name[0] + second_name

#display full name in title case
full_name = f"{first_name} {second_name}"
print(f"Full name: {full_name.title()}")

#displaing the len of the bio
print(f"Length boi: {len(bio)}")

#replacing the boi ("I am" to "I'm")
boi = bio.replace("I am", "I'm")

print(f"First name: {first_name}")
print(f"Second name: {second_name}")
print(f"Username: {username}")
print(f"Boi message: {bio}")

