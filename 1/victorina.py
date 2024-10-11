from random import choice

student = input('Представьтесь, пожалуйста: ')
try:
    level = int(input('Выберите уровень сложности 1 - 5: '))
except:
    level = 1
    print('Установлен 1 уровень сложности.')
if level < 1 or level > 5:
    level = 1
    print('Установлен 1 уровень сложности.')\

animal_easy = ['Кот', 'пес', 'корова', 'лошадь', 'курица']
animal_hard = ['жираф', 'кунгуру', 'носорог', 'панда', 'лягушка']

if level > 3:
    animals = animal_hard
else:
    animals = animal_easy
points = 0
for i in range(5):
    animal = choice(animals)
    print(f'{student}, Угадай животное: это {len(animal)} букв. Оно начинается на "{animal[0]}" и заканчивается на "{animal[-1]}".')
    answer = input('Твой ответ: ')

    if answer == animal:
        points += 1
        print('Правильно!')
    else:
        print(f'Неправльно, это {animal}')
if points == 5:
    print(f'Какой умница, {student}. Это 5!')
elif points >= 3:
    print(f'Так себе, {student}. Можно было лучше.')
else:
    print(f'Плохо, {student}, можешь садиться!')