from sty import fg, rs

class unicornmock():
    def __init__(self):
        self.PHAT = 32
        self.grid = [[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)],[(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]]
        self.brightnesslevel = 0
        self.set_layout(self.PHAT)

    def brightness(self, level):
        self.brightnesslevel = level

    def set_layout(self, formfactor):
        for x in range(8):
            for y in range(4):
                self.grid[y][x] = (0,0,0)

    def set_pixel(self, x, y, r, g, b):
        self.grid[y][x] = r,g,b

    def show(self): 
        for x in range(8):
            for y in range(4):
                r,g,b = self.grid[y][x]
                #print("("+str(r)+","+str(g)+","+str(b)+")")
                print(fg(r,g,b)+"*"+fg.rs, end="")
            print()
