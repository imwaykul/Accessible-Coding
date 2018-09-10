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
    
    

terminal_status = 'CASE UNSOLVED'
terminal_window = Tk()
terminal_window.configure(background='green')
levelSel = Tk()
levelSel.configure(background='blue')
levelSel.withdraw()
levelSel.wm_title("Difficulty Selection")
easyButton = Button(levelSel, text = "Beginner", command = beginnerSelect)
mediumButton = Button(levelSel, text = "Intermediate", command = intermediateSelect)
hardButton = Button(levelSel, text = "Advanced", command = advancedSelect)
easyButton.grid(row = 1, column = 0)
mediumButton.grid(row = 2, column = 0)
hardButton.grid(row = 3, column = 0)

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
terminal_button.grid(row = 0, column = 0)
terminal_description.grid(row = 0, column = 1)
    
intermediate_wind = Tk()
intermediate_wind.configure(background='yellow')
advanced_wind = Tk()
advanced_wind.configure(background='red')
beginner_wind.withdraw()
intermediate_wind.withdraw()
advanced_wind.withdraw()
terminal_window.withdraw()
window.mainloop()
