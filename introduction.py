import pyttsx3;


engine = pyttsx3.init();
count = 0
resp = ""

def intro():
    pass

def hiddenTerminal():
    lives = 5
    questions = []
    new_eng = pyttsx3.init()
    new_eng.say("Mission 1: The Hidden Terminal")
    new_eng.runAndWait()
    new_eng.say("You will have 5 days to finish this mission, so listen up carefully! You will be given a series of tasks to investigate. You lose a day if you incorrectly finish these tasks.")
    new_eng.runAndWait()

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



    
    
