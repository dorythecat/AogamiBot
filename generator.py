import random

pronouns = ["I", "he", "she", "Aogami", "Yosuke", "you", "we", "y'all", "they", "men", "women"]
verbs = ["need", "want", "have", "require", "ask for", "are", "call", "called", "went to" "have come back from",
         "misgender", "misgendered", "gendered", "have", "used", "had", "sexted", "received", "exterminated",
         "watched", "enjoyed", "commited", "hated", "hate", "loved", "love", "kiss", "have kissed", "make love to",
         "got us", "have fucked", "reinstated", "found", "killed", "assasinated", "destroyed", "anhilitaded"]
nouns = ["some Viagra", "some bitches", "a Baja Blast", "a Crunchwrap Supreme", "30 kilograms of refined uranium-235",
         "a maid outfit", "sex", "Aogami", "myself", "Yosuke", "the Persona games", "my schizophrenia", "my pills",
         "my cold metal ass", "a lesbian", "a really hot and sweaty place", "my bed", "your bed", "a slimy place",
         "two maid outfits", "a bag of high-grade peruvian cocaine", "a mariachi band", "Venezuela", "a jar of pickles",
         "a bear", "a woman", "a man", "a hot mess", "some cold food", "a very hot femboy", "a femboy", "a gay old man",
         "Young Man", "a bowl of hot pot", "the soup store", "Sans from Undertale", "Comic Sans, the font",
         "an european 220 volt outlet", "someone's daughter", "the concept of capitalism", "the Soviet Union",
         "the Communist Bloc", "Germany's old glory", "a glory hole", "three kids in a trenchcoat", "Joseph Stalin",
         "John F. Kennedy", "the gays", "lesbophobia", "homophobia", "a random TERF", "two femboys",
         "an undisclosed number of femboys", "Scarlet Johanson", "a cat", "a very handsome butcher",
         "someone's mother", "someone's father", "someone's son", "someone's grandma", "DILFs", "GILFs", "MILFs",
         "Borat", "a tub of mayonnaise", "a strange white liquid", "an undisclosed amout of gay men",
         "Sonic the Hedgehog", "Boris Johnson", "the Western bloc", "anarchism", "BDSM", "Ren", "Zen", "Dory",
         "everyone in this room", "Adolf Hitler", "syphilis", "HIV", "robotic orgasms", "a bench", "gay marriage",
         "trans people", "gender", "Homestuck", "hole", "holes", "none", "**FILE NOT FOUND**", "**ERROR**",
         "sugar daddy", "sugar mommy", "grandma", "grandpa", "father", "mother", "parent", "brother", "sister",
         "girlfriend", "boyfriend"]
adjectives = ["gay", "hot", "indignating", "extreme", "sexy", "robotic", "flamboyant", "autistic", "homophobic",
              "deranged", "gold-digger", "communist", "capitalist", "fucking", "incredible", "bisexual",
              "pansexual", "incredibly upsetting", "upsettingly hot", "not so sexy", "gender", "gender neutral",
              "handsome", "incomprehensible", "possibly upset", "mayhaps fuckable", "boyish", "girlish", "masculine",
              "really fucking gay", "perhaps a lesbian"]
place_verbs = ["let's have sex", "let's build a snowman", "let's kill Hitler", "let's fuck", "let's watch yaoi",
               "let's read", "let's watch random old men", "let's watch the Golden Girls", "let's read erotic novels",
               "let's kiss", "let's buy furtniture", "let's buy a family-sized pizza and eat it alone",
               "I loved her and she loved me"]
places = ["behind the couch", "over on Salzsburg", "in a random alleyway", "in prison", "in a forest",
          "in a random ass house", "in your bed", "in my bed", "in a park", "in my insides", "in your parent's house",
          "in a jacuzzi", "in a nude beach", "in a really hot sauna", "in sexy poses", "in a bench", "in a rusty car",
          "behind your local town's Cotsco", "in a Norweigan IKEA", "underneath the spreading chestnut tree",
          "*singing* on the graves, on the graves, of every girl that I knew before you...", "on a bus"]


def generate() -> str:
    phrase = "Young man, "
    if random.random() > 0.8:
        phrase += random.choice(place_verbs) + " "
        if random.random() > 0.5:
            phrase += random.choice(places)
        return phrase
    pronoun = random.choice(pronouns)
    phrase += pronoun + " "
    if random.random() > 0.5:
        phrase += random.choice(verbs) + " " + random.choice(nouns)
        return phrase
    if pronoun == "I":
        phrase += "am "
    elif pronoun in ["he", "she", "Aogami", "Yosuke"]:
        phrase += "is "
    else:
        phrase += "are "
    phrase += random.choice(adjectives)
    if random.random() > 0.7:
        phrase += " " + random.choice(nouns)
    return phrase


def answer() -> str:
    return random.choice(["Yes", "No", "Absolutely no", "Absolutely yes", "Perhaps", "Maybe", "Surely", "No, u",
                          "Only in Wednesdays", "Perhaps another day", "Not today", "Tomorrow", "Yesterday",
                          "Imagine...", "Only in your imagination", "Pehaps not", "Who knows", "Somedays",
                          "Sometimes", "Only when I'm with you", "Sex", "Only when I see you pinned down in my bed",
                          "Only if you let me see those nips", "Of course", "Of course not", "Only for you",
                          "Everyone", "No one", "Anybody", "A random passerby", "Your mother", "Your sister",
                          "Your father", "Your brother", "You", "Everybody knows", "Violent things",
                          "If you like it or not", "I just want to dance"]) + ", young man"
