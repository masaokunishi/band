class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
class Bassist(object):
    def __init__(self):
        self.sounds = ["Twang", "Thumb", "Bling"]
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Guitarist(object):
    def __init__(self):
        self.sounds = ["Boink", "Bow", "Boom"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
    
    def tune(self):
        print("be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(object):
    def __init__(self):
        self.sounds = ["dondon", "chakachaka", "chinchin"]
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
    def count(self):
        print("1,2,3,4")
        
nigel = Drummer()
nigel.solo(6)
print(nigel.sounds)
nigel.count()


