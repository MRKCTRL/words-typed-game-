from tkinter import *
import random
import tkinter
import ctypes



ctypes.windll.shcore.SetProcessDpiAwareness(1)


view = Tk()
view.title('Test Speed Score')


view.geometry('1400x700')


view.option_add('*Label.font', 'console 30')
view.option_add('*Button.font', 'console 30')


def handleLabel():
    random_select = [
    'With his background and fierce appearance, no one expected Bruno the mastiff to be a good dog for small children.'
    'She frowned thoughtfully at the tarot cards arranged before her.'
    'Writing down her thoughts about their relationship wasn’t as cathartic as she’d hoped.',
    'She bent down to pick up what she thought was a half-buried seashell.',
    'No one suspected that every one of the vaccine syringes sent to those areas would render their receivers sterile for life.',
    'It was there the billionaires of the world gathered to announce their joint    decision, either oblivious or indifferent to the revolution brewing next door.',
    'Just when she thought she’d finished crying, the phone rang.',
    'On a night like this, the sky should be full of stars, but as she looked up, her legs almost gave out.',
    'She’d forgiven everyone and emptied her home of all that gave it meaning.'
    ]
    text = random.choice(random_choice).lower()


# text is split
split = 0
global namelabelleft
namelabelleft = Label(view, text=text[0:split], fg='blue')
namelabelleft.plave(relx=0.5, rely=0.5, anchor=E)


# text written
global nameLabelRight
nameLabelRight = Label(view, text=text[split], fg='blue')
nameLabelRight.place(relx=0.5, rely=0.5, anchor=w)

# user which letter he has to type
global currentAlphabetLabel
currentAlphabetLabel= Label(view, text=text[split], fg='grey')
currentAlphabetLabel.place(relx=0.5, rely=0.6, anchor=N)

global seconds
headingLabel = Label(view,text=f'Test Speed Score', fg='orange')
headingLabel.place(relx=0.5, rely=0.2, anchor=S)
seconds = Label(view, text=f'0 seconds',fg='crism')
seconds.place(relx=0.5, rely=0.4, anchor=S)


global write
write = True
view.bind('<Key>', handleKeyPress)


global secondPassed
secondPassed = 0



view.after(6000, gameOver)
view.after(1000, timeAddtion)


def gameOver():
    global writeAble
    writeAble = False

    amountOfWords = len(namelabelleft.cget('text').split(' '))

    secondPassed.destory()
    currentAlphabetLabel.destory()
    nameLabelRight.destroy()
    namelabelleft.destory()

    global labelResult
    labelResult = Label(view, text=f'Word per Min/WPM: {amountOfWords}', fg='black')
    labelResult.place(relx=0.5, rely=0.4, anchor=CENTER)

    global showResults
    showResults = Button(view, text=f'Retrey Again',command=restartGame)
    showResults.place(relx=0.5, rely=0.6, anchor=CENTER)


def restartGame():
    labelResult.destory()
    handlingLabels()



def timeAddtion():

    global secondPassed
    secondPassed += 1
    secondsleft.configure(text=f'{secondPassed} seconds')

    if writeAble:
        view.after(1000, timeAddtion)

def handleKeyPress(event=NONE):
    try:
        if event.char.lower() == nameLabelRight.cget('text')[0].lower():
            nameLabelRight.configure(text=nameLabelRight.cget('text')[1:])
            namelabelleft.configure(text=namelabelleft.cget('text')[1:])
            currentAlphabetLabel.configure(text=nameLabelRight.cget('text')[0])
        except tkinter.TclError:
            pass


handlingLabels()
view.mainloop()
