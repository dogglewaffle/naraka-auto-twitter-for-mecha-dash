# Auto replying code for naraka bladepoint mecha dash
# First time using python, so code is probally terrable
# Problem is that every couple of hours twitter or the programs goes to a different page and messes up the program and the program must be restart
# May just be a problem with running it on a 2013 bootcamp imac
# Program replys with 1 - 3 words of 500 different words along with a random direction for the character to go to
# Then submits the post and refreshes the page and goes back to the replay box via tab
# Does this 4 times every 2 minutes, with rotating direction words every time
# To start click on the reply box after you click the tweet
import keyboard
import time
import random
# two arrays for random usable words
direction = ["UP", "DOWN", "RIGHT", "LEFT", "LEFT"]
word1 = ["careless", "surround", "bucket", "scrawny", "plate", "ambitious", "holiday", "amuse", "brainy", "concentrate", "tax", "volatile", "expensive", "melodic", "bottle", "weather", "rate", "permit", "extend", "crowded", "religion", "bead", "visitor", "develop", "encourage", "insect", "mass", "skip", "vulgar", "fork", "exist", "hurried", "weak", "decay", "division", "frogs", "flowery", "low", "unlock", "perform", "sniff", "phone", "roll", "nutty", "gate", "automatic", "engine", "glow", "suspend", "understood", "sour", "gentle", "permissible", "jellyfish", "obeisant", "lunchroom", "used", "ashamed", "squeeze", "fireman", "towering", "entertaining", "selective", "groan", "grubby", "scribble", "shelter", "perfect", "enormous", "attractive", "new", "noiseless", "erratic", "pumped", "zip", "ill-fated", "mug", "agreement", "behave", "stomach", "tank", "domineering", "employ", "horse", "cloth", "giant", "ticket", "describe", "road", "wise", "abiding", "thing", "substantial", "habitual", "desk", "arrange", "comb", "design", "paper", "judicious", "earth", "knowing", "decision", "cushion", "sky", "petite", "blushing", "mean", "stage", "normal", "unused", "brawny", "hug", "reason", "field", "descriptive", "cakes", "abortive", "succinct", "meeting", "vast", "bare", "inject", "clam", "cats", "macho", "coat", "chemical", "remarkable", "deliver", "needle", "unique", "nerve", "absorbed", "fax", "bridge", "third", "search", "dad", "donkey", "fill", "royal", "heal", "mysterious", "abnormal", "improve", "space", "harm", "combative", "sail", "warn", "angry", "compare", "rod", "fretful", "noise", "hose", "bizarre", "recognise", "magical", "subsequent", "nut", "encouraging", "flashy", "leg", "pushy", "ants", "fragile", "naive", "lighten", "utter", "tease", "ugly", "quill", "fool", "fearless", "melted", "ball", "sparkle", "change", "bruise", "brief", "even", "jagged", "nasty", "boundless", "amusing", "start", "cactus", "cut", "memory", "pencil", "decorous", "show", "fallacious", "profit", "flash", "medical", "wrong", "adamant", "hard-to-find", "stormy", "point", "pocket", "page", "wiry", "curtain", "dynamic", "enjoy", "discreet", "gun", "stiff", "pen", "well-off", "irritating", "land", "error", "ceaseless", "farm", "hate", "volcano", "panicky", "hair", "afraid", "cheap", "disagree", "fuel", "clumsy", "cluttered", "dress", "weigh", "stamp", "oval", "calculate", "zipper", "numberless", "bolt", "mute", "silent", "selfish", "summer", "linen", "delicious", "safe", "event", "increase", "want", "scattered", "son", "admire", "daughter", "notebook", "violet", "amazing", "argue", "slimy", "afford", "snake", "bathe", "thaw", "tangible", "foot", "claim", "thinkable", "shop", "worm", "replace", "oranges", "hand", "historical", "excuse", "tightfisted", "naughty", "tomatoes", "friend", "smoggy", "tempt", "choke", "unwieldy", "locket", "nail", "hideous", "middle", "vanish", "vegetable", "envious", "eggnog", "wave", "square", "craven", "activity", "fail", "youthful", "lying", "grandiose", "snow", "bang", "camera", "mundane", "interesting", "drag", "acid", "cows", "questionable", "bulb", "furniture", "challenge", "wine", "trip", "lackadaisical", "knowledge", "sign", "melt", "impartial", "entertain", "jump", "zoom", "enchanting", "rainy", "pleasure", "branch", "tan", "grandfather", "absent", "thin", "lacking", "wait", "boiling", "unruly", "succeed", "rambunctious", "juggle", "tranquil", "handsomely", "ambiguous", "moldy", "property", "squeamish", "lip", "burn", "scale", "save", "crown", "sprout", "famous", "relax", "fabulous", "label", "fresh", "sponge", "massive", "double", "spiteful", "uppity", "airport", "nervous", "awful", "star", "ill-informed", "well-made", "strap", "yak", "lonely", "swing", "protective", "giddy", "futuristic", "surprise", "thundering", "whispering", "chance", "berserk", "grouchy", "grip", "van", "hushed", "hunt", "spade", "ignore", "frightening", "admit", "loaf", "minor", "tow", "obey", "puzzled", "shocking", "stupid", "wrist", "squirrel", "useless", "tin", "insurance", "structure", "story", "imminent", "crabby", "payment", "tire", "skillful", "mindless", "suggest", "strengthen", "babies", "remember", "secretive", "hilarious", "sugar", "noisy", "spiky", "thirsty", "credit", "ear", "sea", "pancake", "writing", "wool", "cap", "pets", "whine", "creepy", "spoon", "loose", "offend", "tacit", "best", "lunch", "soup", "complain", "literate", "ultra", "fast", "screeching", "canvas", "lace", "exotic", "self", "bubble", "war", "baby", "wren", "tearful", "madly", "polish", "creator", "weary", "spare", "spiritual", "able", "young", "deer", "discover", "grate", "science", "meat", "zephyr", "water", "grab", "sulky", "vessel", "report", "cow", "acrid", "mixed", "flimsy", "jobless", "laughable", "grain", "blue", "fluttering", "splendid", "dirt", "cannon", "kettle", "hop", "copy", "cover", "hum", "stem", "quizzical", "steam", "doll", "rescue", "books", "inform", "trade", "unaccountable", "righteous", "sleepy", "toy", "shelf", "sick", "advise", "little", "purple", "stare", "crook", "tour", "scientific", "woman"]
#get to where i need to be to start
time.sleep(5)
#initial direction loop variable
j = 3
# Infinate loop
while 1 == 1:
    # uses keyboard to print out  random words
    i = random.randrange(1,3,1)
    while i > 0:
        keyboard.write( word1[random.randrange(0,len(word1) - 1, 1)])
        time.sleep(random.uniform(1.00, 3.00))
        keyboard.write(" ")
        time.sleep(random.uniform(1.50, 4.00))
        i = i - 1
    #direction word with loop to make sure in order 
    keyboard.write( direction[j])
    if j == -1:
        j = 3
    else:
        j = j - 1

    time.sleep(random.uniform(.34, 2.00))
    #post tweet
    keyboard.press_and_release('ctrl+enter')
    time.sleep(random.uniform(3.50, 5.00))
    keyboard.press_and_release('ctrl+shift+r')
    time.sleep(random.uniform(3.50, 5.00))
    i = 0
    #move to input selection
    while i < 20:
        keyboard.press_and_release('tab')
        i = i + 1
        time.sleep(random.uniform(.20, .50))
     #master sleep
    time.sleep(random.uniform(8.0, 10.0))