<<<<<<< HEAD
from units import Missile

_missiles = []
_canvas = None


=======


from units import  Missile
_missiles = []
_canvas = None

>>>>>>> 10a38aa30eedc7db6a97334b5bafb4d32184a4c9
def initialize(canvas):
    global _canvas
    _canvas = canvas

<<<<<<< HEAD

=======
>>>>>>> 10a38aa30eedc7db6a97334b5bafb4d32184a4c9
def fire(owner):
    m = Missile(_canvas, owner)
    _missiles.append(m)

<<<<<<< HEAD

def update():
    start = len(_missiles) - 1
    for i in range(start, -1, -1):
        if _missiles[i].is_destroyed():
            del _missiles[i]
        else:
            _missiles[i].update()

def check_missiles_collision(tank):
    for missile in _missiles:
        if missile.get_owner() == tank:
            continue
        if missile.intersects(tank):
            missile.destroy()
            tank.damage(25)  # Наносим урон танку
            return
=======
def update():
    for missile in _missiles:
        missile.update()

>>>>>>> 10a38aa30eedc7db6a97334b5bafb4d32184a4c9
