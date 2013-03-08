# -*- coding: cp1252 -*-
class PhoneNumber():
  import re

  def __init__(self):
    self.result = []
    self.dictionary = {}
    self.digit_map = ['E', 'JNQ', 'RWX', 'DSY', 'FT', 'AM', 'CIV', 'BKU', 'LOP','GHZ']

  def load_dict(self, fileName):
    file = open(fileName)
    for line in file:
      number = ""
      for letter in self.re.sub('\\n$', '', line).upper():
        for char in self.digit_map:
          if letter in char:
            number += str(self.digit_map.index(char))
            break
      self.dictionary.setdefault(number, []).append(self.re.sub('\\n$', '', line))
    return len(self.dictionary)

  def convertFile(self, fileName):
    file = open(fileName)
    open("TEMP.txt","wb").write("")
    for line in file:
      for section in line.upper().split(', '):
        open("TEMP.txt","a").write(section+"\n")
        
  def convertToNum(self, word):
    result = ""
    for x in word:
      for i in self.digit_map:
        if x.upper() in i:
          result += str(self.digit_map.index(i))
    return result
        
  
  def numbers(self, input):
    input = input
    backup = input
    wordResults = []
    for x in input:
      number = input
      for z in input:
        try:
          wordResults.append(self.dictionary[str(number)])
        except:
          pass
        number = number[:-1]
      input = input[1:]

    final = []
    for x in wordResults:
      for i in x:
        temp = backup
        temp = self.re.sub(self.convertToNum(i) , i , temp)
        for z in wordResults:
          for a in z:
            temp = self.re.sub(self.convertToNum(a) , a , temp)
        if temp not in final:
          final.append(temp)
    return final or "None compatible number"
    

def main():
  a = PhoneNumber()
  #a.convertFile('dict1.txt')
  a.load_dict('dic.txt')
  #print "LOADED"
  print a.numbers('4824')
  print a.numbers('10789135')
  print a.numbers('107835')
  print a.numbers('07372192333')
  #print "DONE"
main()
