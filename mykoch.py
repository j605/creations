from TurtleWorld import *
world = TurtleWorld()
t = Turtle()
t.x = 50
t.y = -50


def mykoch(t,n):
    if n < 1:
        fd(t,100 * n)
        return;
    m = n / 3.0
    mykoch(t,m)
    lt(t,150)
    mykoch(t,m)
           
def mine(t,n):
    for i in range(17):
        mykoch(t,n)
        rt(t,165)   
mine(t,6)
t.die()
world.canvas.dump()
wait_for_user()
