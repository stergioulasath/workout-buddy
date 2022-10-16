#a simple volume calculator to check for the efficiency of your workout today
#you can track and update multiple people

import athlete
from datetime import date

#writes information based on athlete's name
def progressUpdate(person, volume, exercises):

    today = date.today().strftime("%B, %d, %Y")
    with open("progress.txt", "r") as f:
        contents = f.readlines()                    #first we read the contents of the file

    found = False
    for i in contents:
        if i == f"{person.getName()}\n":
            insert = f"{today}\n"
            for v, e in zip(volume, exercises):
                insert += f"Volume for {e}: {v}.\n"        #if athlete already exists, this is what we insert
            insert += "\n"
            
            contents.insert(contents.index(i)+1, insert)
            found = True
            break
        
    if found == False:
        insert = f"{person.getName()}\n{today}:\n"     #if athlete doesn't exist, create new entry
        for v, e in zip(volume, exercises):
            insert += f"Volume for {e}: {v}.\n"
        insert += "\n"
            
        contents.insert(0, insert)
    

    with open("progress.txt", "w") as f:
        contents = "".join(contents)                 #we write it in the file
        f.write(contents)


def check(a, b, c):
    return a*b*c > 0


def main():
    
    name, weight = input("Enter your name and weight.").split()
    person = athlete.person(name, weight)
    volume = []
    exercises = []
    currentvolume = 0
    while True:
        exercise = input('Name of the exercise you are tracking? Type "0" to cancel tracking.')
        if (exercise == "0"):
            break
        
        numbers = str(input("Enter number of Sets, number of Reps, and number of Kilos lifted. Type 0 to switch exercise."))
        while numbers != "0":
            numbers = numbers.split()
            sets = int(numbers[0])
            reps = int(numbers[1])
            kilos = int(numbers[2])
            if check(sets, reps, kilos): #sets, reps, kilos 
                currentvolume += person.calculateVolume(sets, reps, kilos)
                volume.append(currentvolume)
            numbers = str(input("Enter number of Sets, number of Reps, and number of Kilos lifted. Type 0 to switch exercise."))
        
        else:
            exercises.append(exercise)
            currentvolume = 0
            
    progressUpdate(person, volume, exercises)


main()
