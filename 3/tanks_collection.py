from random import randint
from units import Tank
import world
from missilies_collection import check_missile_collision
_tanks = []
_canvas = None


def initialize(canv):
    global _canvas
    _canvas = canv
    # spawn(False)
    # for i in range(1):
    #     spawn(True).set_target(get_player())
    player = spawn(False)
    enemy = spawn(True).set_target(player)
    spawn(True).set_target(player)


def get_player():
    return _tanks[0]

def update():
    start = len(_tanks) - 1
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i != 0:
            del _tanks[i]
        else:
            _tanks[i].update()
            check_collision(_tanks[i])
            check_missile_collision(_tanks[i])
    #for tank in _tanks:
        #tank.update()
        #check_collision(tank)
        #check_missile_collision(tank)

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