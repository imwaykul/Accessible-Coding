from tkinter import *


name = ""
gender = ""
difficulty = ""

def register():
    global gender
    global name
    name = name_entry.get()
    #print(name)
    #print(gender)
    if (len(name) > 0 and len(gender) > 0):
        print("Welcome ", name)
        introToDifficultySel()
    else:
        print("Missing Crucial Information!")
        
    
        

def genderSelectMale():
    global gender
    gender = "M"
    print(gender)

def genderSelectFemale():
    global gender
    gender = "F"

def introToDifficultySel():
    global window
    global levelSel
    window.withdraw()
    levelSel.deiconify()
    

def beginnerSelect():
    global difficulty, levelSel
    difficulty = "B"
    levelSel.withdraw()
    beginner_wind.deiconify()

def intermediateSelect():
    global difficulty
    difficulty = "I"

def advancedSelect():
    global difficulty
    difficulty = "A"

def terminal_start():
    global beginner_wind, terminal_window
    beginner_wind.withdraw()
    terminal_window.deiconify()

def addTextToBeginning():
    global levelSel, start_text, continueButton
    levelSel.withdraw()
    nextText = "Click 'Continue' to visit your log book. Here you can view your cases, as well as your scare & status for each case. We got high expectations for you Rookie!"
    secondRow = Label(levelSel, text = nextText, background = "blue")
    secondRow.grid(row = 1, column = 0)
    levelSel.deiconify()
    levelSel.withdraw()
    finalText = "Good Luck Out There!!"
    thirdRow = Label(levelSel, text = finalText, background = "blue")
    thirdRow.grid(row = 2, column = 0)
    continueButton.configure(text = "Continue", command = beginnerSelect)
    levelSel.deiconify()
    
    
    

terminal_status = 'CASE UNSOLVED'
terminal_window = Tk()
terminal_window.configure(background='green')
levelSel = Tk()
levelSel.configure(background='blue')
levelSel.withdraw()
levelSel.wm_title("Difficulty Selection")
#easyButton = Button(levelSel, text = "Beginner", command = beginnerSelect)
#mediumButton = Button(levelSel, text = "Intermediate", command = intermediateSelect)
#hardButton = Button(levelSel, text = "Advanced", command = advancedSelect)
continueButton = Button(levelSel, text = "Next", command = addTextToBeginning, background = "blue")
#easyButton.grid(row = 1, column = 0)
#mediumButton.grid(row = 2, column = 0)
#hardButton.grid(row = 3, column = 0)
print("NAME: ", name)
start_text = "Welcome " + name + " to your first set of cases! We're glad to have you on the job. Since you're just a rookie, you'll need some training before you go out and solve cases"

descriptionLabel = Label(levelSel, text = start_text, background = "blue")
descriptionLabel.grid(row = 0, column = 0)
continueButton.grid(row = 3, column = 0)


window = Tk()
window.wm_title("Interrogation Room")
window.configure(background='black')
name_entry = Entry(window)
name_entry.insert(0, "your name")
mainButton = Button(window,text="Submit", command= register)
maleButton = Button(window,text="Male", command= genderSelectMale)
femaleButton = Button(window,text="Female", command= genderSelectFemale)
name_entry.grid(row = 0, column = 0)
mainButton.grid(row = 0, column = 1)
maleButton.grid(row = 1, column = 0)
femaleButton.grid(row = 1, column = 1)

beginner_wind = Tk()
beginner_wind.configure(background='green')
beginner_wind.wm_title("Welcome Rookie")

terminal_button = Button(beginner_wind, text = "Terminal", command = terminal_start, background = 'green')
terminal_description = Label(beginner_wind, text = terminal_status, background = 'green')

primitives_button = Button(beginner_wind, text = "Primitives", command = terminal_start, background = 'green')
primitives_description = Label(beginner_wind, text = terminal_status, background = 'green')

variables_button = Button(beginner_wind, text = "Variables", command = terminal_start, background = 'green')
variables_description = Label(beginner_wind, text = terminal_status, background = 'green')

functions_button = Button(beginner_wind, text = "Functions", command = terminal_start, background = 'green')
functions_description = Label(beginner_wind, text = terminal_status, background = 'green')

return_n_print_button = Button(beginner_wind, text = "Variables", command = terminal_start, background = 'green')
return_n_print_description = Label(beginner_wind, text = terminal_status, background = 'green')

mathcalc_button = Button(beginner_wind, text = "Math Calculuations", command = terminal_start, background = 'green')
mathcalc_description = Label(beginner_wind, text = terminal_status, background = 'green')

terminal_button.grid(row = 0, column = 0)
terminal_description.grid(row = 0, column = 1)
primitives_button.grid(row = 1, column = 0)
primitives_description.grid(row = 1, column = 1)
variables_button.grid(row = 2, column = 0)
variables_description.grid(row = 2, column = 1)
functions_button.grid(row = 3, column = 0)
functions_description.grid(row = 3, column = 1)
return_n_print_button.grid(row = 4, column = 0)
return_n_print_description.grid(row = 4, column = 1)
mathcalc_button.grid(row = 5, column = 0)
mathcalc_description.grid(row = 5, column = 1)


    
intermediate_wind = Tk()
intermediate_wind.configure(background='yellow')
advanced_wind = Tk()
advanced_wind.configure(background='red')
beginner_wind.withdraw()
intermediate_wind.withdraw()
advanced_wind.withdraw()
terminal_window.withdraw()
window.mainloop()
