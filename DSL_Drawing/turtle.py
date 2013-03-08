import math
class turtle():
    def __init__(self, obj):
        self.Interface = obj
        self.Y = 150
        self.X = 150
        self.Pen = True
        self.For = False
        self.Angle = 0
        self.History = []
        self.Change = 0
        
    def parseCode(self, change=None):
        if change == None:
            code = str(self.Interface.getCode()).split('\n')
        else:
            code = change
	loopFunctions = []
	cache = []
	iterations = 0
        for f in code:
            if 'move_back()' in f:
                self.move_back();
            elif 'move_forward()' in f:
                self.move_forward();                
            elif 'for' in f:
                cache.append(f)
                self.For = True
                iterations = f.split(' ')[-2]
            elif f.split('(')[0] in self.__class__.__dict__.keys():
                cache.append(f)
                if self.For:
                    loopFunctions.append('self.'+f)
                else:
                    eval('self.'+f)
            elif 'end' in f:
                cache.append(f)
                self.For = False
                for x in range(int(iterations)):
                    for f in loopFunctions:
                        eval(f)
                loopFunctions.pop()
            else: print("unknown command: " +f)
        if self.Change == 0:
            self.History.append(cache)
        
                        
    def move(self, steps, angle):
        self.Angle += angle
        angle = self.Angle - 90
        if(angle < 0): angle = 360 + angle
        radius = angle * math.pi / 180.0
        for i in range(steps):
            self.X += math.cos(radius)
            self.Y += math.sin(radius)
            if self.Pen: self.Interface.setPixel(int(self.X), int(self.Y))
            if self.Change == 1: self.Interface.unsetPixel(int(self.X), int(self.Y))
            if self.Change == 2: self.Interface.setPixel(int(self.X), int(self.Y))
    def move_back(self):
        self.Change = 1
        a = self.History[0]
        self.parseCode(a)
        self.Change = 0
    def move_forward(self):
        self.Change = 2
        a = self.History[0]
        self.parseCode(a)
        self.Change = 0
    def turn_cw(self, angle):
        self.Angle += angle  
    def turn_ccw(self, angle):
        self.Angle -= angle 
    def pen_down(self):
        self.Pen = True
    def ped_up(self):
        self.Pen = False
    def put(self, x, y, angle):
        self.Y = y
        self.X = x
        self.Angle = angle
    
