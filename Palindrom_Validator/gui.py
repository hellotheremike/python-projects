# -*- coding: cp1252 -*-

import Tkinter
import tkMessageBox

root = Tkinter.Tk()

inputData = Tkinter.Entry(root, width = 10, bg='white', font=('arial', 14))
resultLbl = Tkinter.Label(root, text='Resultat:', font=('arial', 9), fg='black')
infoLbl = Tkinter.Label(root, height = 1,text='Ange grader i farenheit', font=('arial', 9) ,fg='black')

def main(): 
    GUI()
    root.mainloop()

def GUI():
    root.title('Palindrom Kontroll')
    root.geometry('350x150')

    infoLbl.grid(row=0, column=1)
    resultLbl.grid(row=1, column=2)
    inputData.grid(row=1, column=1)

    Tkinter.Button(root, width = 20, text = "Konvertera ",bg = "GREY", command = show_result).grid(row=2, column=1)
    Tkinter.Button(root, width = 20, text = "Spara ",bg = "GREY", command = save).grid(row=3, column=1)
    Tkinter.Button(root, width = 20, text = "Avsluta ",bg = "GREY", command = quitProg).grid(row=4, column=1)


def save():
    text = show_result()
    if text:
        myFile = open('palindrom.txt', 'a')
        try:
            myFile.write(text + '\n')
        except IOError:
            tkMessageBox.showwarning('Error', 'Ett fel uppstod!\nDet gick inte att skriva till filen.')
    else:
        tkMessageBox.showwarning('Error', 'Ett fel uppstod!\nDu måste ange ett palindrom för att kunna spara!')

def show_result():
    text = inputData.get().upper()
    x = ""
    if text != '': 
        for arrayDeleteChar in text:
            if arrayDeleteChar in '!,.?#%&/()=*^" ':
                arrayDeleteChar = ""
            x += arrayDeleteChar 
        y = x[::-1]

        if x == y:
            resultLbl.config(text='Grattis, '+str(text)+' är ett palindrom')
            resultLbl.config(bg='green')
        else:
            resultLbl.config(text='Tyvär, '+str(text)+' är inte ett palindrom')
            resultLbl.config(bg='red')
    else:
        resultLbl.config(text='Skriv in ett ord eller en fras')
        resultLbl.config(bg='red')

def quitProg():
    root.destroy()
    
if __name__ == '__main__': 
    main()  
