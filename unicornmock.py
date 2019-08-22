class unicornmock:
    def __init__(self):
        self.PHAT = 32
        self.grid = []
        self.brightnesslevel = 0
        self.set_layout(self.PHAT)

    def brightness(self, level):
        self.brightnesslevel = level

    def set_layout(self, formfactor):
        for x in range(8):
            for y in range(4):
                self.grid[x,y] = 0,0,0

    def set_pixel(self, x, y, r, g, b):
        self.grid[x,y] = r,g,b

    def show(self): 
        for x in range(8):
            for y in range(4):
                print("("+self.grid[x,y]+")")
