class Mario():

    def move(self):
        print("I am movingg..")



class Shroom():

    def eat_shroom(self):
        print("Now I am big!")


# We can't just leave the class empty normally. It gives an error. So to get over it. We call 'pass'.
class BigMario(Mario, Shroom):
  pass

bm = BigMario()
bm.move()
bm.eat_shroom()

