import pyttsx3;


engine = pyttsx3.init();
count = 0
resp = ""
finishedOne = 0

def incorrect(engine, n):
    engine.say("I'm afraid that's not right, you have lost a day, and currently have " + str(n) + " days to solve this case")
    engine.runAndWait()


def correct(engine):
    engine.say("Great work! That is absolutely right, onto the next task.")
    engine.runAndWait()


def intro():
    pass
    
    
def hiddenTerminal():
    lives = 5
    tasks = ["First, you'll need to find exactly what terminal Cole Yates is currently in. To do this, you'll have to go to the 'Terminal' itself. If you're on a Mac, you go to a search bar and type in what?",
             "Perfect, Cole just sent a text, here's what it says: 'Yeah I'll be around Magnolia Section'. Great, lets head over there. Now that we've reached, we need to keep a journal of clues. For this mission, you'll need to do all your work in terminal. To do this we need to make a folder called CodingDetective. What command allows us to do that",
             "Nice, but you're on the 5th floor you need to navigate below to the fourth floor to meet Cole, what command allows you to do this? ", "Perfect, you've reached Cole, now see what he has planned"]
    correctAnswers = ["terminal", "mkdir", "cd", "C"]
    description1 = "Last night, a precious and priceless artifact called 'The Golden Luxury'" + "has been stolen. We believe this is connected to a string of burglaries that have occurred over the past 5 months." +"While we did catch a few of these thieves, none of them have spilled a word about either their motives nor their group identity" +"However, this morning, we got an anonymous tip from a witness at the Bellguard Train Station who witnessed the group meeting. We need you to go there, and interrogate this witness" +"Fair warning, he didn't seem like the kind of person to openly talk, unless he is given an incentive. So please, do anything he may ask you to do. We believe in you private, good luck!"
    new_eng = pyttsx3.init()
    new_eng.say("Mission 1: The Hidden Terminal")
    new_eng.runAndWait()
    new_eng.say("You will have 5 days to finish this mission, so listen up carefully! You will be given a series of tasks to investigate. You lose a day if you incorrectly finish these tasks. Please press D to get a description of the mission after this message.")
    new_eng.runAndWait()
    desc = input("Press D to get a description of the mission")
    while (desc != "D" and desc != "d"):
        desc = input()
    new_eng.say(description1)
    new_eng.runAndWait()
    count = 0
    while (count < len(tasks)):
        if (lives == 0):
            new_eng.say("I'm sorry, Cole has left the station and is no longer interested in communicating with us. Please try this mission again.")
            new_eng.runAndWait()
            break
        new_eng.say(tasks[count])
        new_eng.runAndWait()
        new_eng.say("Type out the answer to this question : ")
        new_eng.runAndWait()
        answer = input("Select the correct answer")
        if (answer != correctAnswers[count]):
            lives = lives - 1
            incorrect(new_eng, lives)
        if (answer == correctAnswers[count]):
            correct(new_eng)
            count = count + 1
    repeat = "T"
    while (repeat != "N" and repeat != "n"):
        repeat = input("Would you like this repeated?")
        new_eng.say("I can only entrust you with information if I think you're capable of handling what i'm about to say. I need you to do the following things for me. ")
        new_eng.runAndWait()
        new_eng.say("Don't press N to continue, press N to hear the message again")
        new_eng.runAndWait()
    repeat = "T"
    while (repeat != "N" and repeat != "n"):
        repeat = input("Would you like this repeated?")
        new_eng.say("This next portion requires you to use the terminal on your computer. Open it on the side, and listen to the instructions")
        new_eng.runAndWait()
        new_eng.say("Don't press N to continue, press N to hear the message again")
        new_eng.runAndWait()
    repeat = "T"
    while (repeat != "N" and repeat != "n"):
        repeat = input("Would you like this repeated?")
        new_eng.say("First, navigate to the directory or folder that you wish. hint using cd and ls helps")
        new_eng.runAndWait()
        new_eng.say("Press N to continue, press any other button to hear the message again")
        new_eng.runAndWait()
    repeat = "T"
    while (repeat != "N" and repeat != "n"):
        repeat = input("Would you like this repeated?")
        new_eng.say("Next, create a folder and name it CodingDetective")
        new_eng.runAndWait()
        new_eng.say("Press N to continue, press any other button to hear the message again")
        new_eng.runAndWait()
    repeat = "T"
    while (repeat != "N" and repeat != "n"):
        repeat = input("Would you like this repeated?")
        new_eng.say("Now, navigate to the coding detective")
        new_eng.runAndWait()
        new_eng.say("Press N to continue, press any other button to hear the message again")
        new_eng.runAndWait()
    repeat = "T"
    while (repeat != "N" and repeat != "n"):
        repeat = input("Would you like this repeated?")
        new_eng.say("Create a file named Lesson1.py")
        new_eng.runAndWait()
        new_eng.say("Press N to continue, press any other button to hear the message again")
        new_eng.runAndWait()
    repeat = "T"
    while (repeat != "N" and repeat != "n"):
        repeat = input("Would you like this repeated?")
        new_eng.say("Finally, download the following file titled GreetingsAgent dot py, save it in the directory and run the file from the terminal")
        new_eng.runAndWait()
        new_eng.say("Press N to continue, press any other button to hear the message again")
        new_eng.runAndWait()
    repeat = "T"
    
    
    
    


    
        
    

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



    
    
