<<<<<<< HEAD
from tkinter import NW
from random import randint
from missiles_collection import check_missiles_collision
=======
from random import randint
>>>>>>> 10a38aa30eedc7db6a97334b5bafb4d32184a4c9
from units import Tank
import world
from missilies_collection import check_missile_collision
_tanks = []
_canvas = None

id_screen_text=0
def initialize(canv):
    global _canvas, id_screen_text
    _canvas = canv
<<<<<<< HEAD

    player = spawn(False)
    for _ in range(5):  # Создаем 5 танков противников
        enemy = spawn(True)
        enemy.set_target(player)
    id_screen_text = _canvas.create_text(10, 10, text=_get_screen_text(), font=('TkDefaultFont', 20), fill='white', anchor=NW)

def _get_screen_text():
    if get_player().is_destroyed():
        return 'Потрачено'
    if len(_tanks) == 1:
        return 'победа'
    return 'Осталось {}'.format(len(_tanks)-1)

def _update_screen_text():
    _canvas.itemconfig(id_screen_text, text=_get_screen_text())
=======
    # spawn(False)
    # for i in range(1):
    #     spawn(True).set_target(get_player())
    player = spawn(False)
    enemy = spawn(True).set_target(player)
    spawn(True).set_target(player)
>>>>>>> 10a38aa30eedc7db6a97334b5bafb4d32184a4c9


def get_player():
    return _tanks[0]

def update():
<<<<<<< HEAD
    _update_screen_text()

    start =len(_tanks) - 1
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i !=0:
=======
    start = len(_tanks) - 1
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i != 0:
>>>>>>> 10a38aa30eedc7db6a97334b5bafb4d32184a4c9
            del _tanks[i]
        else:
            _tanks[i].update()
            check_collision(_tanks[i])
<<<<<<< HEAD
            check_missiles_collision(_tanks[i])
=======
            check_missile_collision(_tanks[i])
    #for tank in _tanks:
        #tank.update()
        #check_collision(tank)
        #check_missile_collision(tank)
>>>>>>> 10a38aa30eedc7db6a97334b5bafb4d32184a4c9

def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return True
    return False



def spawn(is_bot=True):
    cols = world.get_cols()
    rows = world.get_rows()

    while True:
        col = randint(1, cols-1)
        row = randint(1, rows-1)

        if world.get_block(row, col) != world.GROUND:
            continue

        t = Tank(_canvas, row,col, bot=is_bot)
        if not check_collision(t):
            _tanks.append(t)
            return t