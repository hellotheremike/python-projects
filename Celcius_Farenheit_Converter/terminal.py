# -*- coding: cp1252 -*-
#Sätter en global variabel
grader = ''

def main():
    repeat = 'j'
    while repeat == 'j':
        global grader
        grader = raw_input('Grader grader i Fahrenheit: ')
        fahrenheitCelsius()
        
        repeat = raw_input('Köra programmet engång till? j / n: ')
        print '--------------------------------------------'
    
def fahrenheitCelsius():
    """
    Testar om det går att räkna ut ekvationen.
    Om du skulle mata in någonting som inte är ett
    numeriskt värde, alltså som inte går att konvertera till ett flyttal, 
    returerar den false och kör koden under catch
    """
    try:
        result = (float(grader)/2-16.00)*10/9
        print str(grader), ' grader Farenheit blir, ', str(round(result, 2)), 'grader Celsius'
    except:
        print 'Endast heltal eller flyttal, t.ex) -1.23 eller 2'
        main()
main()
