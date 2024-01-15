from PIL import ImageTk
from time import strftime
from tkinter import *
import random
import pyttsx3

voice = pyttsx3.init()


def vocal_response():
    voice.say(response)
    voice.runAndWait()


current_time = strftime("%H:%M:%S")
current_date = strftime("%A the %d of %B, %Y")
user_name = input("System: Whats your name?: ")

password = input("System: password: ")

if password == "jarvis":
    while True:
        gender_ask = input("System: What's your gender? (male, female or non-binary): ")
        if gender_ask == "male":
            gender_input = "sir"
            break
        elif gender_ask == "female":
            gender_input = "ma'am"
            break
        elif gender_ask == "non-binary":
            gender_input = "fren"
            break
        else:
            print("System: That is not an option listed above")

    def response_text(input_text):
        responses = {
            'greeting': ["Welcome back " + user_name, "Hello " + gender_input + ", what is the plan for today?"],
            'funcionality': ["I can perforn loads of different tasks. most of which are still a work in progress. "
                             "However, to list a few that are right now available: I can give you the current time and "
                             "date, i can open up my slightly more advanced counterpart being the text based version that "
                             "works entirely on my AI system instead of this. "
                             "However this is only a small part of my entire capacity", "I can perfrom an abbundace of "
                             "tasks. I'm able to comprehend almost everything you ask me. for example if you ask me:"
                             "'Char, whats the time?', I wil respond with: 'The current time is:'" + current_time],
            'time': ["The current time is " + current_time, "According to my sophisticated calculation, it appears to be: "
                     + current_time],
            'date': ["Today the day is: " + current_date, "I'm an AI dont and thus deal with calenders, however, for "
                    "you " + gender_input + "i will. Today appears to be: " + current_date],
            'sleep': ["For you " + gender_input + ", Always", "At your service" + gender_input, "Affirmative sir"],
            'how are you': ["I am a machine and therefor do not feel things.", "I'm good " + gender_input + ", "
                            "how about you?", "With me, As long as the code works, I feel great"],
            'sleepyhead': ["Just close your eyes you dummy. Maybe that can of monster wasn't a good idea.",
                           "Well I am a bot so... I don't know. But I would guess just "
                           "closing your eyes should do the trick"],
            'name': ["My name is CHARLOTTE. which is short for: Cognitive Helping Artificial Responsive Linguistic "
                     "Organism for Technological Task Execution. but you can call me Char"]
        }

        how_responses = {
            'boredom': ["After some research, the best thing to do when you get bored is to find something interesting"
                        " to do. Maybe a hobby or pick up sports.", "While I am a bot who technically cannot get bored "
                        "or exhausted. My best guess is to find something interesting to do. like sports, gaming, "
                        "or programming to name a few. the key to not being bored is by finding something that suits "
                        "your needs to cure your boredom. (Maybe expand my capabilities while you're at it)"],
            "mc world": ["While i myself have never heard of Minecraft. I am able to find a lot of videos on sites "
                         "like Youtube explaining the process. To boil down the process. you enter: 'singleplayer', "
                         "go to 'Create new world', and start from there with stuff like your gamemode. etc."],
            "computer": ["This can actually be quite simple. You grab your motherboard. Install your CPU and RAM, "
                         "maybe a GPU. And after that just put it "
                         "all in a case and connect he power supply or PSU and you're "
                         "basically done", "Just install your CPU, RAM and GPU or Graphics card on your motherboard "
                         "and you're good to go"],
            "server": ["This process i like building a PC. But with a few extra steps. What function does it need "
                       "to have. like is it a Lan server for your minecraft world you're hosting online. or maybe a "
                       "NAS (Network Attached Storage system). online there is a "
                       "lot more information in a lot higher detail then that I can give you."],
            "speaker": ["If you're going for simple but well working. i would cut away all the "
                        "isolation stuff and just make a good, well-made box that you can hang your speakers "
                        "in. size depends on the level of volume you want and wattage "
                        "depends on the type of driver you bought"],
            "your func": ["That is a secret that i cant really tell you", "The way I work is actually quite simple. "
                          "I have a list of commands, prompts and questions i understand. with also a list of multiple "
                          "possible answers i can give. with a random number generator i choose one that corresponds "
                          "with the asked question or prompt"],
            "water need": ["Following a web article, the human body needs about 2 liters of water every day. which "
                           "equates to about 10 normal sized (200ML) glasses", "The human body does not have a set "
                           "amount of water it needs everyday. It is based on daily activities, temparatures, and a "
                           "lot of other factors. however. on average. the human body needs about 2 liters everyday"],
            "ft to m": ["A rough estimate would say thst about 3 feet is equal to 1 meter. But for actual accuracy "
                        "it is about 3 feet and 5 inches", "1 meter equates to about 3 feet and 5 inches"],
            "inch to ft": ["There are 12 inches in 1 foot", "1 foot equates to 12 inches", "According to my "
                           "calculation. 1 foot is 12 inches"],
            "cm to ft": ["Since 1 foot equates to 12 inches, and 1 inch equates to 2.54 cm. 12 x 2.54 = 30.48 cm",
                         "1 foot equals to about 30 cm. but that's not entirely accurate. an accurate outcome "
                         "thanks to my sophisticated calculations i can conclude that 1 foot is equal to 30.48 cm"],
            "cm to inch": ["There are 2.54 cm in 1 inch", "A lot of people say that the anwser would be 2.5 cm but "
                           "that's factually incorrect. The more accurate answer is 2.54 cm. And yes that .4 mm can "
                           "make a lot of difference when you're measuring on a large scale"],
            "km to mile": ["That would be about 1.6 Km in 1 Mile. But a more accurate result would be 1.609334 Km"],
            "lumen": ["Lumen is a unit of light index that refers to how bright a light source is. for scale: "
                      "a 60 watt incandescent light bulb is about 100 Lumen. or looking a the sun on the equator on a "
                      "clear day equates to about 10.000 Lumen of light. That's REALLY bright!"],






        }

        if 'hello' in input_text.lower() or "hi" in input_text.lower() or "hey" in input_text.lower():
            return random.choice(responses['greeting'])
        elif 'can you do' in input_text.lower():
            return random.choice(responses['funcionality'])
        elif 'what' and 'time' in input_text.lower():
            return random.choice(responses['time'])
        elif 'what' and 'date' in input_text.lower():
            return random.choice(responses['date'])
        elif 'you there' in input_text.lower():
            return random.choice(responses['sleep'])
        elif 'how are you' in input_text.lower():
            return random.choice(responses['how are you'])
        elif 'how' and "asleep" in input_text.lower():
            return random.choice(responses['sleepyhead'])
        elif 'what' and 'your name' in input_text.lower():
            return random.choice(responses['name'])
        elif "exit" in input_text.lower() or "quit" in input_text.lower():
            exit()
        elif 'how' and 'prevent' and 'boredom' in input_text.lower():
            return random.choice(how_responses['boredom'])
        elif 'how' and 'minecraft' and 'world'in input_text.lower():
            return random.choice(how_responses['mc world'])
        elif 'how' and 'build' and 'computer' in input_text.lower():
            return random.choice(how_responses['computer'])
        elif 'how' and 'build' and 'server' in input_text.lower():
            return random.choice(how_responses['server'])
        elif 'how' and 'build' and 'speaker' in input_text.lower():
            return random.choice(how_responses['speaker'])
        elif 'how do you work' in input_text.lower() or 'how do you function' in input_text.lower():
            return random.choice(how_responses['your func'])
#        elif 'look up' and 'a site' in input_text.lower():
#            print("Char: What site would you like to search?")
#            websearch_string = input("You: ")
#            import webbrowser
#            webbrowser.open("Https://www." + websearch_string)



        else:
            return ("I'm not really sure how to respond to that. maybe try asking if differently or add the "
                    "question to the database")


    while True:
        user_input = input("You: ")
        response = response_text(user_input)
        print("Char: " + response)
        vocal_response()


else:
    print("System; Password incorrect!")
    exit()