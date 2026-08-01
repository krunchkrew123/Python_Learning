# Goal is to write my first program in Python!
# Using the reference material from the other projects, and not following a tutorial


import random

# Make an array using the Legends from the game Apex legends
apex_legends = [
    "Wraith",
    "Bangalore",
    "Bloodhound",
    "Caustic",
    "Crypto",
    "Gibraltar",
    "Lifeline",
    "Mirage",
    "Octane",
    "Pathfinder",
    "Wattson",
    "Revenant",
    "Loba",
    "Rampart",
    "Horizon",
    "Fuse",
    "Valkyrie",
    "Seer",
    "Ash",
    "Mad Maggie",
    "Newcastle",
    "Vantage",
    "Catalyst",
    "Ballistic",
    "Conduit",
    "Alter"
]

legend_quips = {
    "Wraith": 'Tell death I said hello.',
    "Crypto": "I'm the only one who can see the future.",
    "Pathfinder": "Losing isn't fun. That's why I don't do it."
}

ready = input('Are you ready to select a random Apex Legend? (yes/no): ')

if ready.lower() == 'yes':
    selected_legend = random.choice(apex_legends)
    print(f'Challenge accepted! Your Legend is: {selected_legend}')
    if selected_legend in legend_quips:
        print(legend_quips[selected_legend])
elif ready.lower() == 'no':
    no = input('Are you sure? (yes/no): ')
    if no.lower() == 'yes':
        print('Skill issue...')
        quit()
    else:
        print('Ok bet, good choice;)')
else:
    print('Invalid input. Please enter "yes" or "no".')



