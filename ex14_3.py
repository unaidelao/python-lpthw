from sys import argv

script, first_name, last_name = argv
prompt = 'prompt -> '

print(f"Hi!, I'm the {script} script.")
print(f"I'd like to ask you a few questions {first_name} {last_name}.")
print(f"Do you like cakes {first_name}?")
likes = input(prompt)

print(f"Where do you live {first_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking cakes.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")