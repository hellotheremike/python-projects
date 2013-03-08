import math
class turtle():
    def __init__(self, obj):
        self.Interface = obj
        self.Y = 100
        self.X = 100
        self.Pen = True
        self.Angle = 0
        
    def parseCode(self):
        code = str(self.Interface.getCode())
	code = code.split('\n')
        for f in code:
            #print callable(eval("self."+f))
            eval("self."+f)
        
    def mov1e(self, steps, angle):
        rad = angle * (math.pi/180)
        x = math.sin(rad)
        y = math.cos(rad)
        ratio = x/y
        print ratio
        for x in range(self.X, (steps+self.X)):
            self.X = x
            self.Y = x*ratio
            self.interface.setPixel(x , int(x*ratio))

    def move(self, steps, angle):
        self.Angle += angle
        for i in range(steps):
            self.Angle += angle
            self.X += self.getX(self.Angle)
            self.Y += self.gety(self.Angle)
            if self.Pen:
                self.Interface.setPixel(int(self.X), int(self.Y))
        
    def getX(self, angle):
        angle -= 90
        if(angle < 0):
            angle = 360 + angle
        angle = angle * math.pi / 180.0
        return math.cos(angle)
    def gety(self, angle):
        angle -= 90
        if(angle < 0):
            angle = 360 + angle
        angle = angle * math.pi / 180.0
        return math.sin(angle)


    def put(self, x, y):
        self.Y = y
        self.X = x
