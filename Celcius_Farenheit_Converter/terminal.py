# -*- coding: cp1252 -*-
#S�tter en global variabel
grader = ''

def main():
    repeat = 'j'
    while repeat == 'j':
        global grader
        grader = raw_input('Grader grader i Fahrenheit: ')
        fahrenheitCelsius()
        
        repeat = raw_input('K�ra programmet eng�ng till? j / n: ')
        print '--------------------------------------------'
    
def fahrenheitCelsius():
    """
    Testar om det g�r att r�kna ut ekvationen.
    Om du skulle mata in n�gonting som inte �r ett
    numeriskt v�rde, allts� som inte g�r att konvertera till ett flyttal, 
    returerar den false och k�r koden under catch
    """
    try:
        result = (float(grader)/2-16.00)*10/9
        print str(grader), ' grader Farenheit blir, ', str(round(result, 2)), 'grader Celsius'
    except:
        print 'Endast heltal eller flyttal, t.ex) -1.23 eller 2'
        main()
main()
