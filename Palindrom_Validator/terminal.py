# -*- coding: cp1252 -*-

def main():
    repeat = 'j'
    while repeat == 'j':
        #B�rjar med att konvertera texten till
        #uppercase eftersom den �r casesensetive i if-satsen 
        text = raw_input("Mata in ett ord: ").upper()
        x = ""
        print '------------------------------------'

        for a in text:
            print a+' ['+str(i)+']'
            if a in '!,.?#%&/()=*^" ':
                a = ""

            x += a
       
        y = x[::-1]
        
        print '------------------------------------'
        print x, 'blir, ', y, ' bakl�nges'
        
        if x == y:
            print "True, detta �r ett palindrom"
        else:
            print "False, detta �r inte ett palindrom"

        
        print '------------------------------------'
        repeat = raw_input('K�ra programmet eng�ng till? j / n: ')

main()
