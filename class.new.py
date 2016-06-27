class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()
        
class Bassist(object):
    def __init__(self):
        self.sounds = ["Twang", "Thumb", "Bling"]
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

class Guitarist(object):
    def __init__(self):
        self.sounds = ["Boink", "Bow", "Boom"]

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()
    
    def tune(self):
        print("be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(object):
    def __init__(self):
        self.sounds = ["dondon", "chakachaka", "chinchin"]
    
    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()
        
    def count(self):
        print("1,2,3,4")
   
#Bands should be able to hire and fire musicians, and have the musicians play 
#their solos after the drummer has counted time.        
class Band(object):
    def __init__(self):
        self.members = {}

    def hire(self):
        new_member = raw_input("What's the new member's name? ")
        type_of_musician = raw_input("Is he a drummer or a guitarist (lower case)? ")
        if type_of_musician == "drummer":
            self.members[new_member] = Drummer()
        elif type_of_musician == "guitarlist":
            self.members[new_member] = Guitarist()
            
    def fire(self,fired_member):
        del self.members[fired_member]
        
    def play_solos(self,length):
        for v in self.members.itervalues():
            band_has_drummer = isinstance(v,Drummer)
            break
        if band_has_drummer:
            print("There is a drummer")
            for musician in self.members.itervalues():
                musician.solo(length)
                musician.combust()
        else:
            print("There is no drummer")
            for musician in self.members.itervalues():
                musician.solo(length)

def main():
    thebeatles = Band()
    thebeatles.hire()
    thebeatles.hire()
    thebeatles.hire()
    thebeatles.fire("Ringo")
    print(thebeatles.members)
    thebeatles.play_solos(6)
    
if __name__ == "__main__":
    main()


