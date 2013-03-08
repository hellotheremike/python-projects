class animal():
    def __init__(self, n, s):
        self.name = n
        self.spicies = s
    def name(self):
        return self.name
    def spicies(self):
        return self.spicies

class animals:
    def __init__(self):
        self.x = []
        a1 = animal("bob", "dog")
        a2 = animal("jack", "dog")
        a3 = animal("Frodo", "hobbit")
        a4 = animal("Sam", "cat")
        self.x = [a1, a2, a3, a4]

    def get(self, pos):
        return self.x[pos]
    def new(self, obj):
        self.x.append(obj)
    def size(self):
        return len(self.x)

class HashTable:
    class obj():
        def __init__(self, key, value):
            self.key = key
            self.value =  value
            self.next = None     
        def next(self, obj):
            self.next = obj
        def next(self):
            return self.next
    
    def __init__(self):
        self.size = 13
        self.array = [None]*self.size
            
    def add(self, key, value):
        if self.array[self.hashit(key)] == None:
            val = self.obj(key, value)
            self.array[self.hashit(key)] = val
        else:
            o = self.findNext(self.array[self.hashit(key)])
            val = self.obj(key, value)
            o.next = val

    def findNext(self, obj):
        if obj.next == None:
            return obj
        else:
            return n(obj.next)

    def findKey(self,obj, key):
        if(obj.key == key):
            return obj
        else:
            return obj.next
            
    def get(self, key):
        if self.array[self.hashit(key)] == None:
            return 0
        else:
            o = self.array[self.hashit(key)]
            if(o.key == key):
                return o.value
            else:
                return self.findKey(o, key).value
            

    def hashit(self, key):
        if key == None:
            return 0
        else:
            n = 0
            for a in key:
                n += ord(a)
            n = n % self.size
            return n
