# -*- coding: cp1252 -*-

import Tkinter
import tkMessageBox
msg = tkMessageBox
root = Tkinter.Tk()

inputData = Tkinter.Entry(root, width = 10, bg='white', font=('arial', 14))
resultLbl = Tkinter.Label(root, height = 1,text='Resultat:', font=('arial', 9), fg='black')
infoLbl = Tkinter.Label(root, height = 1,text='Ange grader i farenheit', font=('arial', 9) ,fg='black')

def main(): 
    GUI()
    root.mainloop()

def GUI():
    root.title('Farenheit till Celsius konverterare')
    root.geometry('350x100')
    infoLbl.grid(row=0, column=1)
    resultLbl.grid(row=1, column=2)
    inputData.grid(row=1, column=1)

    Tkinter.Button(root, width = 15,  text = "Konvertera ",bg = "GREY", command = corr).grid(row=2, column=1)
    Tkinter.Button(root, width = 15, text = "Avsluta ",bg = "GREY", command = quit_prog).grid(row=3, column=1)


def corr():
    pass
                
def quit_prog():
    root.destroy()
    
if __name__ == '__main__': 
    main()  
