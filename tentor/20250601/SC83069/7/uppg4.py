class BlobCreature:
    def __init__(self, energy):
        self.energy = energy
    
    def feed(self, amount):
        self.energy += amount
    
    def split(self):
        if self.energy >= 100.0:
            self.energy /= 2
            return BlobCreature(self.energy)
        
        return None
