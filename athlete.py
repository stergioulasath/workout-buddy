
class person:

    def __init__(self):
        pass

    def __init__(self, name, kg):
        self.name = name
        self.kg = kg

    def getName(self):
        return str(self.name)
    
    def getWeight(self):
        return int(self.kg)

    def calculateVolume(self, sets, reps, kg):
        return sets*reps*kg
    

    




