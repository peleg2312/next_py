from animals import Animal,Dog, Cat, Skunk, Unicorn, Dragon

def main():
    animal_list = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky", 0),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
    ]
    #יצירת מערך עצמים

    for animal in animal_list:
        if animal.is_hungry():
            print(f"{animal.__class__.__name__} {animal.get_name()}")
            while animal.is_hungry():
                animal.feed()
        #אם החיה רעבה אז מאחיל אותה עד שאין רעב
        animal.talk()
        #מדפיס את מה שהחיה אומרת
        if isinstance(animal, Dog):
            animal.fetch_stick()
        #אם הוא כלב מדפיס פעולה מיוחדת של כלב
        elif isinstance(animal, Cat):
            animal.chase_laser()
            #אם הוא חתול מדפיס פעולה מיוחדת של חתול
        elif isinstance(animal, Skunk):
            animal.stink()
        #אם הוא בועש מדפיס פעולה מיוחדת של בועש
        elif isinstance(animal, Unicorn):
            animal.sing()
        #אם הוא חד קרן מדפיס פעולה מיוחדת של חד קרן
        elif isinstance(animal, Dragon):
            animal.breath_fire()
        #אם הוא דרקון מדפיס פעולה מיוחדת של דרקון

    print(f"Zoo name: {Animal.zoo_name}")
#מדפיס את שם גן החיות
main()
