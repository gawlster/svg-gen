#!/usr/bin/env python3
'''Assignment 4 Part 3 template'''
print(__doc__)

import random
from typing import List, Tuple, IO

class Circle:
    ''' Circle class '''
    def __init__(self, cir: Tuple[int, int, int, int], col: Tuple[int, int, int, float]):
        '''__init__ method'''
        '''
            cir: (cx_coordinate, cy_coordinate, radius)
            col: (red_percentage, green_percentage, blue_percentage, opacity)
        '''
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        
    def get_center(self):
        '''get_center method'''
        return (self.cx, self.cy)
    
    def get_radius(self):
        '''get_radius method'''
        return self.rad
    
    def get_color(self):
        '''get_color method'''
        return (self.red, self.green, self.blue)
        
    def get_opacity(self):
        '''get_opacity method'''
        return self.op
    
    def set_center(self, center):
        '''set_center method'''
        self.cx = center[0]
        self.cy = center[1]
    
    def set_color(self, color):
        '''set_color method'''
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        self.op = color[3]
    
    def print_shape(self):
        '''print_shape method'''
        print("Circle = ", end="")
        print(self.get_center(), end=" ")
        print(self.get_radius(), end=" ")
        print(self.get_color())
    
    def draw_shape(self, f):
        '''draw_shape method'''
        ts: str = "   " # * t
        line: str = f'<circle cx="{self.get_center()[0]}" cy="{self.get_center()[1]}" r="{self.get_radius()}" fill="rgb{self.get_color()}" fill-opacity="{self.get_opacity()}"></circle>'
        f.write(f"{ts}{line}\n")
#?################   END CIRCLE CLASS   #################
          
class Ellipse:
    ''' Ellipse class '''
    def __init__(self, eli: Tuple[int, int, int, int], col: Tuple[int, int, int, float]):
        '''
        eli: (x_coordinate, y_coordinate, radius_x, radius_y)
        col: (red_percentage, green_percentage, blue_percentage, opacity)
        '''
        self.ex: int = eli[0]
        self.ey: int = eli[1]
        self.rx: int = eli[2]
        self.ry: int = eli[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
    
    def get_center(self) -> Tuple[int, int]:
        '''get_center method'''
        return (self.ex, self.ey)
    
    def get_radius(self) -> Tuple[int, int]:
        '''get_radius method'''
        return (self.rx, self.ry)
    
    def get_color(self):
        '''get_color method'''
        return (self.red, self.green, self.blue)
    
    def get_opacity(self):
        '''get_opcaity method'''
        return self.op
    
    def set_center(self, center):
        '''set_center method'''
        self.ex = center[0]
        self.ey = center[1]
    
    def set_color(self, color):
        '''set_color method'''
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        self.op = color[3]
    
    def print_shape(self):
        '''print_shape method'''
        print("Ellipse= ", end="")
        print(self.get_center(), end=" ")
        print(self.get_radius(), end=" ")
        print(self.get_color())
    
    def draw_shape(self, f):
        '''draw_shape method'''
        ts: str = "   " # * t
        line: str = f'<ellipse cx="{self.get_center()[0]}" cy="{self.get_center()[1]}" rx="{self.get_radius()[0]}" ry="{self.get_radius()[1]} fill="rgb{self.get_color()}" fill-opacity="{self.get_opacity()}"></ellipse>'
        f.write(f"{ts}{line}\n")
#?################   END ELLIPSE CLASS   #################
         
class Rectangle:
    ''' Rectangle class '''   
    def __init__(self, rect: Tuple[int, int, int, int], col: Tuple[int, int, int, float]):
        '''__init__ method'''
        '''
           rect: (rx_coordinate, ry_coordinate, width, height) **coordinates are from top left corner
           col: (red_percentage, green_percentage, blue_percentage, opacity) 
        '''
        self.rx: int = rect[0]
        self.ry: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        
    def get_top_left(self):
        '''get_top_left method'''
        return (self.rx, self.ry)
    
    def get_width(self):
        '''get_width method'''
        return self.width
        
    def get_height(self):
        '''get_height method'''
        return self.height
    
    def get_color(self):
        '''get_color method'''
        return (self.red, self.green, self.blue)
        
    def get_opacity(self):
        '''get_opacity method'''
        return self.op
    
    def set_top_left(self, coordinate):
        '''set_top_left method'''
        self.rx = coordinate[0]
        self.ry = coordinate[1]
    
    def set_color(self, color):
        '''set_color method'''
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        self.op = color[3]
    
    def print_shape(self):
        '''print_shape method'''
        print("Rectangle = ", end="")
        print(self.get_top_left(), end=" ")
        print(self.get_width(), end=" X ")
        print(self.get_height(), end=" ")
        print(self.get_color())
    
    def draw_shape(self, f):
        '''draw_shape method'''
        ts: str = "   " # * t
        line: str = f'<rect x="{self.get_top_left()[0]}" y="{self.get_top_left()[1]}" width="{self.get_width()}" height="{self.get_height()}" fill="rgb{self.get_color()}" fill-opacity="{self.get_opacity()}"></rect>'
        f.write(f"{ts}{line}\n")
#?################   END RECTANGLE CLASS   #################
          
class ProEpilogue:
    '''ProEpilogue class'''
    def __init__(self, fname="myPart3Art.html", winTitle="My Art", shape_data_list=[], viewport_x=500, viewport_y=500):
        '''__init__ method'''
        f: IO[str] = open(fname, "w")
        self.f = f
        self.writeHTMLHeader(f, winTitle)
        self.openSVGcanvas(f, 1, (viewport_x,viewport_y))
        shapes_list = create_shapes(shape_data_list)
        draw_shapes(self, shapes_list)
        self.closeSVGcanvas(f, 1)
        f.close()
        
    def writeHTMLHeader(self, f: IO[str], winTitle: str):
        '''writeHeadHTML method'''
        self.writeHTMLline(f, 0, "<html>")
        self.writeHTMLline(f, 0, "<head>")
        self.writeHTMLline(f, 1, f"<title>{winTitle}</title>")
        self.writeHTMLline(f, 0, "</head>")
        self.writeHTMLline(f, 0, '<body style="margin:0; overflow:hidden">')
        
    def writeHTMLline(self, f: IO[str], t: int, line: str):
        '''writeLineHTML method'''
        ts = "   " * t
        f.write(f"{ts}{line}\n")
        
    def openSVGcanvas(self, f: IO[str], t: int, canvas: tuple):
        '''openSVGcanvas method'''
        ts: str = "   " * t
        self.writeHTMLcomment(f, t, "Define SVG drawing box")
        f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')
        
    def closeSVGcanvas(self, f: IO[str], t: int):
        '''closeSVGcanvas method'''
        ts: str = "   " * t
        f.write(f'{ts}</svg>\n')
        f.write(f'</body>\n')
        f.write(f'</html>\n')
        
    def writeHTMLcomment(self, f: IO[str], t: int, com: str):
        '''writeHTMLcomment method'''
        ts: str = "   " * t
        f.write(f'{ts}<!--{com}-->\n')
#?################   END PROEPILOGUE CLASS   #################
        
def draw_shapes(canvas, shape_list):
    '''draw_shapes method'''
    for shape in shape_list:
        shape.draw_shape(canvas.f)
               
def create_shapes(shape_data_list):
    '''create_shapes method'''
    shape_list = []
    for i in range(len(shape_data_list)):
        cur_shape = shape_data_list[i]
        cur = cur_shape.shape_details
        if cur[0] == 0:
            cir = (cur[1], cur[2], cur[3])
            col = (cur[8], cur[9], cur[10], cur[11])
            shape_list.append(createCircle(cir, col))
        elif cur[0] == 1:
            rect = (cur[1], cur[2], cur[6], cur[7])
            col = (cur[8], cur[9], cur[10], cur[11])
            shape_list.append(createRectangle(rect, col))
        elif cur[0] == 2:
            eli = (cur[1], cur[2], cur[4], cur[5])
            col = (cur[8], cur[9], cur[10], cur[11])
            shape_list.append(createEllipse(eli, col))
        
    return shape_list

def createCircle(cir, col):
    '''createCircle method'''
    return Circle(cir, col)

def createRectangle(rect, col):
    '''createRectangle method'''
    return Rectangle(rect, col)
    
def createEllipse(eli, col):
    '''createEllipse method'''
    return Ellipse(eli, col)

class ArtConfig:
    '''ArtConfig class'''
    def __init__(self, viewport_x, viewport_y):
        '''__init__ method'''
        self.viewport_x = viewport_x
        self.viewport_y = viewport_y
        self.shape: int = self.getRandomShapeIndex()
        self.x, self.y = self.getRandomCoordinates()
        self.rad: int = self.getRandomRadius()
        self.rx, self.ry = self.getRandomRxRy()
        self.width, self.height = self.getRandomWidthHeight()
        self.red, self.green, self.blue, self.op = self.getRandomColor()
        self.shape_details = (self.shape, self.x, self.y, self.rad, self.rx, self.ry, self.width, self.height, self.red, self.green, self.blue, self.op)
    
    def getRandomShapeIndex(self) -> int:
        '''getShapeIndex method'''
        lower_bound: int = 0
        upper_bound: int = 2
        return random.randint(lower_bound, upper_bound)
        
    def getRandomCoordinates(self) -> Tuple[int, int]:
        '''getRandomCoordinates method'''
        lower_bound: int = 0
        upper_bound: int = self.viewport_x
        x: int = random.randint(lower_bound, upper_bound)
        upper_bound: int = self.viewport_y
        y: int = random.randint(lower_bound, upper_bound)
        return (x, y)
    
    def getRandomRadius(self) -> int:
        '''getRandomRadius method'''
        lower_bound: int = 0
        upper_bound: int = 100
        return random.randint(lower_bound, upper_bound)
    
    def getRandomRxRy(self) -> Tuple[int, int]:
        '''getRandomRxRy method'''
        lower_bound: int = 10
        upper_bound: int = 30
        return (random.randint(lower_bound, upper_bound), random.randint(lower_bound, upper_bound))
    
    def getRandomWidthHeight(self) -> Tuple[int, int]:
        '''getRandomWidthHeight method'''
        lower_bound: int = 10
        upper_bound: int = 100
        return (random.randint(lower_bound, upper_bound), random.randint(lower_bound, upper_bound))
    
    def getRandomColor(self) -> Tuple[int, int, int, float]:
        '''getRandomColor method'''
        color_list: List[int] = []
        lower_bound: int = 0
        upper_bound: int = 255
        for i in range(3):
            color_list.append(random.randint(lower_bound, upper_bound))
        upper_bound: int = 1.0
        color_list.append(random.random())
        color_tup: Tuple[int, int, int, float] = tuple(color_list)
        return color_tup
#?################   END ARTCONFIG CLASS   #################

class GenRandom:
    '''Gen Random class'''
    count: int = 0
    def __init__(self, viewport_x=500, viewport_y=500, num_shapes=10):
        '''__init__ method'''
        self.viewport_x: int = viewport_x
        self.viewport_y: int = viewport_y
        self.shape_list: List[ArtConfig] = []
        for i in range(num_shapes):
            self.count += 1
            shape: ArtConfig = ArtConfig(viewport_x, viewport_y)
            self.shape_list.append(shape)
        
    def print_table(self) -> None:
        '''print_table method'''
        print('CNT  SHA    X    Y  RAD   RX   RY    W    H    R    G    B   OP')
        for i in range(self.count):
            cur_shape: ArtConfig = self.shape_list[i]
            cur: Tuple[int, int, int, int, int, int, int, int, int, int, int, float] = cur_shape.shape_details
            print(f'{i:3d}  {cur[0]:3d}  {cur[1]:3d}  {cur[2]:3d}  {cur[3]:3d}  {cur[4]:3d}  {cur[5]:3d}  {cur[6]:3d}  {cur[7]:3d}  {cur[8]:3d}  {cur[9]:3d}  {cur[10]:3d}  {cur[11]:0.1f}')
    
    def get_shapes_list(self) -> List[ArtConfig]:
        '''get_shapes_list method'''
        return self.shape_list
#?################   END GENRANDOM CLASS   #################
        
        
def main():
    '''main method'''
    randoms = GenRandom(viewport_x=500, viewport_y=900, num_shapes=100000)
    shape_list = randoms.get_shapes_list()
    ProEpilogue(shape_data_list=shape_list, viewport_x=1920, viewport_y=1080)

main()