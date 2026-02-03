class duck:
    def sound(self):
        print("QUACK QUACK:")
class dog:
    def sound(self):
        print("boww boww:")
class cat:
    def sound(self):
        print("meow meow:")
def allsounds(obj):
    obj.sound()
d=dog()
allsounds(d)