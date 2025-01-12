class Animal:
    def speak(self):
        print('Животное говорит')

class BigDog(Animal):
    def speak(self):
        print('Большая, гав-гав!')

class SmGog(Animal):
    def speak(self):
        print('Маленькая, гав!')

class ToyDog(SmGog):
    def speak(self):
        print('Игрушечная, 0111001')

class BigAngryDog(BigDog):
    def speak(self):
        print('Злой взгляд!')
        super().speak()
        print('Хмурится')

class Cat(Animal):
    def _meow(self):
        print('Мяу!')
    def speak(self):
        self._meow()

class NCat(Cat):
    def _meow(self):
        print('Mau!')

def say_n_times(animal, times):
    for _ in range(times):
        animal.speak()
druzok = BigAngryDog()
say_n_times(druzok, 3)
print('-------------------')
list_of_animals = [Cat(), ToyDog(), BigAngryDog()]
for animal in list_of_animals:
    animal.speak()

#animal = Animal()
#animal.speak()
#bd = BigDog()
#bd.speak()
#sm = SmGog()
#.speak()
#td = ToyDog()
#td.speak()
#sharik = BigAngryDog()
#sharik.speak()
print('-------------------')
vaska = Cat()
vaska.speak()
vask = NCat()
vask.speak()

