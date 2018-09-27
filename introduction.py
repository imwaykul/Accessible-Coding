import pyttsx3;

engine = pyttsx3.init();
count = 0
resp = ""

def intro():
    pass

def helloDetective():
    pass
    
    

def hiddenTerminal():
    lives = 3
    tasks = ["First, you'll need to find exactly what terminal Cole Yates is currently in. To do this, you'll have to go to the 'Terminal' itself. If you're on a Mac, you go to a search bar and type in what?",
             "Perfect, Cole just sent a text, here's what it says: 'Yeah I'll be around Magnolia Section'. Great, lets head over there. Now that we've reached, we need to keep a journal of clues. For this mission, you'll need to do all your work in terminal. To do this we need to make a folder called CodingDetective.",
             "Nice, but you're on the 5th floor you need to navigate below to the fourth floor to meet Cole, what command allows you to do this? ", "Perfect, you've reached Cole, now see what he has planned"]
    correctAnswers = ["terminal", "mkdir", "cd"]
    description1 = "Last night, a precious and priceless artifact called 'The Golden Luxury'" + "has been stolen. We believe this is connected to a string of burglaries that have occurred over the past 5 months." +"While we did catch a few of these thieves, none of them have spilled a word about either their motives nor their group identity" +"However, this morning, we got an anonymous tip from a witness at the Bellguard Train Station who witnessed the group meeting. We need you go there, and interrogate this witness" +"Fair warning, he didn't seem like the kind of person to openly talk, unless he is given an incentive. So please, do anything he may ask you to do. We believe in you private, good luck!"
    new_eng = pyttsx3.init()
    new_eng.say("Mission 1: The Hidden Terminal")
    new_eng.runAndWait()
    new_eng.say("You will have 5 days to finish this mission, so listen up carefully! You will be given a series of tasks to investigate. You lose a day if you incorrectly finish these tasks.")
    new_eng.runAndWait()
    desc = input("Press D to get a description of the mission")
    while (desc != "D" and desc != "d"):
        desc = input()
    new_eng.say(description1)
    new_eng.runAndWait()
    print("MISSION START!")
        
    

while (resp != "c" and resp != "C"):
    engine.say("Hi There");
    engine.runAndWait() ;
    engine.say("This is the start of your first case Private, get ready")
    engine.runAndWait() ;
    engine.say("After you have read the lesson on terminals, press 'C' to start the mission")
    engine.runAndWait() ;
    engine.say("Press 'R' To repeat the explanation, Press 'C' to move on to your first case")
    engine.runAndWait() ;
    resp = input("Are you ready? ")
    while ( resp != "r" and resp != "R" and resp != "c" and resp != "C"):
        resp = input()
        c = c + 1
    print("FINALL VALUE OF RESP: ", resp)
    
        
hiddenTerminal()



    
    
