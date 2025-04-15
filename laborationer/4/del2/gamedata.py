
DESCRIPTIONS = {
    "Start": """You enter a room, and you see a blue door to your left and a \
red door to your right.
Which door do you pick?""",
    "Blue": """You see a room with a wooden treasure chest on the left, and a \
sleeping guard on the right in front of the door.
What do you do?""",
    "Chest": """Let's see what's in here... /grins
The chest creaks open, and the guard is still sleeping. That's one heavy \
sleeper! You find some diamonds, a shiny sword, and lots of gold coins.
Do you take the treasure or leave it?""",
    "Take": """Woohoo! Bounty and a shiney new sword. /drops your crappy \
sword in the empty treasure chest.
Ooops! The noise has woken up the guard.
What do you do now?""",
    "Leave":
    """Leaving all the shinies behind hurts, but it feels safer for now.
Hopefully, it will still be here, right after you gets past this guard.
What do you do next?""",
    "Guard": """The guard seems to be deep in sleep, but he has a mean \
looking axe right beside him.
What do you do?""",
    "Left": """The guard jumps up and looks the other way, missing you \
entirely.
You just slipped through the door before the guard realised it.
You are now outside, home free! Huzzah!""",
    "Talk": """The guard approaches you and swings his axe, and your world \
goes dark...""",
    "Red": """There you see the great evil Slathborg.
He, it, whatever stares at you and you go insane.
Do you flee for your life or attack it with your bare hands?""",
    "Flee": """You made it out alive, alas empty handed.""",
    "Attack": """You died. Well, at least the dragon thought you were tasty""",
    "Direction": """Do you want to go left or right?""",
    "Right": """The guard approaches you and swings his axe, and your world \
goes dark...""",
    "Joke": """You tell the guard a hilarious joke, and he lets you pass for being so witty!"""
}

OPTIONS = {
    "Blue": "Blue",
    "Red": "Red",
    "Chest": "Explore the chest",
    "Guard": "Advance toward the guard",
    "Take": "Grab all of the treasures",
    "Leave": "Leave them for another day",
    "Sneak": "Try to sneak past the guard",
    "Talk": "Talk to the guard",
    "Flee": "Flee",
    "Attack": "Attack",
    "Joke": "Tell a joke"
}

ADVENTURE_TREE = {
    "Start": ["Blue", "Red"],
    "Blue": ["Chest", "Guard"],
    "Chest": ["Take", "Leave"],
    "Take": ["Sneak", "Talk", "Joke"],
    "Sneak": ["Direction"],
    "Direction": ["Left", "Right"],
    "Left": ["End"],
    "Right": ["End"],
    "Talk": ["End"],
    "Leave": ["Sneak", "Talk", "Joke"],
    "Guard": ["Sneak", "Talk", "Joke"],
    "Red": ["Flee", "Attack"],
    "Flee": ["End"],
    "Attack": ["End"],
    "Joke": ["End"]
}