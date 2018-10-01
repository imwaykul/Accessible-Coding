#Mission 2: "Primitive Yet Priceless"
#Topic: Primitives: ints, float, string, boolean
#Suspect: Selena Goldsman

#1. You Enter The Manufacturing Company
#2. Goldsman asks you to sign in with the Front-Desk
#3. TASK 1: write your name on a nametag.let nametag be a variable, suppose you want to set your name to the value nametag, what type is name tag?(30 minutes)
#4. TASK 2: please set nametag to contain the value of your name.(2 hours)
#5. Meet with Selena; elaborate 
#6. TASK 3: set b = $100, 
#7. TASK 4: Math equation- y = (b * 12 - 50)
#--------------------------------------------------------------

import pyttsx3
import math
import random
engine = pyttsx3.init()

def init():
    response = "r"
    while (response.lower() == "r"):
        engine.say("Mission 2: Primitive Yet Priceless")
        engine.runAndWait()
        engine.say("You will be given 6 hours for this task. " +
                   "However, understand that some tasks may take longer than others. " +
                   "Should you fail tasks that require a lot of time, you will pay the price dearly")
        engine.runAndWait()
        engine.say("Click anything but the button 'r' to continue, unless you want this section repeated")
        engine.runAndWait()
        response = input("Click 'r' to repeat the introduction")

question_counter = 1
hours = 6
penalty = [0.5, 2, 1, 1, 0.1, 0.2, 3, 0.5, 1]

def part_one():
    global penalty, hours, question_counter 
    engine = pyttsx3.init()
    engine.say("Selena Goldsman is 40 and the entrepreneur of a manufacturing company GoldenGlass, with the motto Primitive yet Priceless. She’s always been a person who’s questioned everything; how does it work, what purpose does it serve, and more importantly how can i make it more efficient. The company claims that the glass, while using minimal material, is not only aesthetic but extremely sturdy. Several Quality Analysis tests have confirmed this. But the most recent robbery, along with 2 other robberies in the past 5 months are the only cases where the glass broke. What’s up with that")
    engine.runAndWait()
    



def incorrect(hrs, n):
    minutes = int((n * 60) % 60)
    hours = math.floor(n)
    hrs_pen = hrs - math.ceil(n)
    min_pen = 60 - minutes
    if (minutes == 0 and hours != 0):
        engine.say("I'm afraid that's not right, you have lost " + str(hours) + "hours , and currently have " + str(hrs_pen) + " hours to interrogate Goldsman")
        engine.runAndWait()
    elif (minutes != 0 and hours == 0):
        engine.say("I'm afraid that's not right, you have lost " + str(minutes) + "minutes , and currently have " + str(hrs_pen) + " hours and " + str(min_pen) + " minutes to interrogate Goldsman.")
        engine.runAndWait()
    else:
        engine.say("I'm afraid that's not right, you have lost " + str(hours) + "hours and " + str(minutes) + "minutes , and currently have " + str(hrs_pen) + " hours and " + str(min_pen) + " minutes to interrogate Goldsman.")
        engine.runAndWait()
        
def missionFail():
    engine.say("I'm sorry, the factory has shutdown, and you can no longer interrogate Ms. Goldsman. You'll have to try another day. Mission Failed.")
    engine.runAndWait()

def speak_rand_num():
    n = random.randrange(10, 20)
    engine.say(str(n))
    engine.runAndWait()
    
def correct():
    engine.say("Great work! That is absolutely right, onto the next task.")
    engine.runAndWait()

##use .strip() or a method to remove useless spaces
answers = {1: "string",
           2: "nametag=",
           3: "b=100",
           4: "y=b*12-50"}

#ANSWERS:
#1. String
#2. nametag = "[Insert your name]"
#init()
#part_one()
#incorrect(6, 0.15)
#missionFail()
speak_rand_num()
