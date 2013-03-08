# -*- coding: cp1252 -*-

def main():
    repeat = 'j'
    while repeat == 'j':
        #Börjar med att konvertera texten till
        #uppercase eftersom den är casesensetive i if-satsen 
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
        print x, 'blir, ', y, ' baklänges'
        
        if x == y:
            print "True, detta är ett palindrom"
        else:
            print "False, detta är inte ett palindrom"

        
        print '------------------------------------'
        repeat = raw_input('Köra programmet engång till? j / n: ')

main()
