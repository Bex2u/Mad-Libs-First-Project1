import math
import random
adjective1 = input("Give an adjective or type r for random:\n")
noun1 = input("Give a noun or type r for random:\n")
name = input("Give a name or type r for random:\n")
past_tense_verb1 = input("Past tense verb or type r for random:\n")
adjective2 = input("Give an adjective or type r for random:\n")
adjective3 = input("Give an adjective or type r for random:\n")
noun2_recurring = input("Give a noun or type r for random:\n")
past_tense_verb2  =input("Past tense verb or type r for random:\n")
adjective4 = input("Give an adjective or type r for random:\n")
past_tense_verb3 = input("Past tense verb or type r for random:\n")
present_tense_verb1 = input("Present tense verb or type r for random:\n")
adjective5 = input("Give an adjective or type r for random:\n")
adjective6 = input("Give an adjective or type r for random:\n")
adjective7  = input("Give an adjective or type r for random:\n")
plural_noun1 = input("Give a plural noun or type r for random:\n")
adjective8 = input("Give an adjective or type r for random:\n")
plural_noun2 = input("Give a plural noun or type r for random:\n")
verb1 = input("Give a verb or type r for random:\n")
adjective9 = input("Give an adjective or type r for random:\n")
verb2 = input("Give a verb:\n")
sound_effect = input("Make up a sound effect:\n")
past_tense_verb4 = input("Past tense verb:\n")
noun3 = input("Give a noun:\n")
adjective_emotion = input("Give an adjective (emotion):\n")
adjective10 = input("Give an adjective:\n")
adjective11  = input("Give an adjective:\n")
past_tense_verb5 = input("Past tense verb:\n")
adjective12 = input("Give one last adjective:\n")

adjective_list = ['quirky', 'tall', 'short', 'red', 'blue', 'upset', 'trusty', 'problematic', 'vibrant', 'serene', 'spooky', 'happy', 'mysterious']
noun_list = ['apple', 'bird']
plural_noun_list  =['apples', 'birds']
past_tense_verb_list = ['ran', 'walked']
present_tense_verb_list = ['running', 'walking']
verb_list = ['run', 'walk']
name_list = ['Becker', 'Arjun', 'Gullible']
sound_effect_list = ['zoinks', 'bonks']




if adjective1 == 'r':
    print(random.choice(adjective_list))
if noun1 == 'r':
    print(random.choice(adjective_list))
if name == 'r':
    print(random.choice(name_list))
if past_tense_verb1 == 'r':
    print(random.choice(past_tense_verb_list))
if adjective2 == 'r':
    print(random.choice(adjective_list))
if adjective3 == 'r':
    print(random.choice(adjective_list))
if noun2_recurring == 'r':
    print(random.choice(noun_list))
if past_tense_verb2 == 'r':
    print(random.choice(past_tense_verb_list))
if adjective4 == 'r':
    print(random.choice(adjective_list))
if past_tense_verb3 == 'r':
    print(random.choice(past_tense_verb_list))
if present_tense_verb1 == 'r':
    print(random.choice(present_tense_verb_list))
if adjective5 == 'r':
    print(random.choice(adjective_list))
if adjective6 == 'r':
    print(random.choice(adjective_list))
if adjective7 == 'r':
    print(random.choice(adjective_list))
if plural_noun1 == 'r':
    print(random.choice(plural_noun_list))
if adjective8 == 'r':
    print(random.choice(adjective_list))
if plural_noun2 == 'r':
    print(random.choice(plural_noun_list))
if adjective2 == 'r':
    print(random.choice(adjective_list))
if verb1 == 'r':
    print(random.choice(verb_list))
if adjective9 == 'r':
    print(random.choice(adjective_list))
if verb2 == 'r':
    print(random.choice(verb_list))
if sound_effect == 'r':
    print(random.choice(sound_effect_list))
if past_tense_verb4 == 'r':
    print(random.choice(past_tense_verb_list))
if noun3 == 'r':
    print(random.choice(noun_list))



print(f"\nStory:\nMining Away\nWritten by Becker Viteri and Arjun Vazir and You!:\n\tOnce upon at time, a(n) {adjective1} {noun1} named {name} wanted to get rich, so he {past_tense_verb1} away to a cave to mine some {adjective2} minerals. With his {adjective3} pickaxe and {noun2_recurring} in hand, he {past_tense_verb2} to the mines. Once he arrived, he took a {adjective4} breath and {past_tense_verb3} in. As {name} was {present_tense_verb1}, he found a(n) {adjective5} spot, so he took out his pickaxe and swung it at the {adjective6} stone. After a few swings of his pickaxe, {name} spotted something {adjective7}.\n\t{plural_noun1}! Exactly what he was looking for! Using his {adjective8} {plural_noun2}, he successfully harvested it. However, it was at this moment when the cave started to {verb1} heavily. If {name} didn't do something soon, he would be {adjective9}! That is when {name} had an idea. Using his {noun2_recurring} from earlier, {name} was able to successfully {verb2} out of the cave. 'Well, {sound_effect}!' {name} said. 'That's the last time I'll be mining again.' So {name} {past_tense_verb3} to his {noun3}, {adjective_emotion} to start his new day. When {name} finally got to his {adjective10} home, he put away his {adjective11} spoils and {past_tense_verb4} to his bed. As he shut his eyes, he drifted off into a sweet sleep, wondering what other {adjective12} adventures were in store for the next day.\n\tThe end.")