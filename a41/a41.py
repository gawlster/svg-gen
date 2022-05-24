#!/usr/bin/env python3
'''Assignment 4 Part 1 template'''
print(__doc__)

from typing import IO

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
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
        return (self.red, self.green, self.blue, self.op)
        
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
    
    def print_circle(self):
        '''print_circle method'''
        print("Circle = ", end="")
        print(self.get_center(), end=" ")
        print(self.get_radius(), end=" ")
        print(self.get_color)
    
    def draw_shape(self, f):
        '''draw_shape method'''
        ts: str = "   " # * t
        line: str = f'<circle cx="{self.get_center()[0]}" cy="{self.get_center()[1]}" r="{self.get_radius()}" fill="rgb{self.get_color()}" fill-opacity="{self.get_opacity()}"></circle>'
        f.write(f"{ts}{line}\n")
        
        
        
        
class Rectangle:
    '''Rectangle class'''   
    def __init__(self, rect:tuple, col:tuple):
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
    
    def print_rectangle(self):
        '''print_rectangle method'''
        print("Rectangle = ", end="")
        print(self.get_top_left(), end=" ")
        print(self.get_width(), end=" X ")
        print(self.get_height(), end=" ")
        print(self.get_color)
    
    def draw_shape(self, f):
        '''draw_shape method'''
        ts: str = "   " # * t
        line: str = f'<rect x="{self.get_top_left()[0]}" y="{self.get_top_left()[1]}" width="{self.get_width()}" height="{self.get_height()}" fill="rgb{self.get_color()}" fill-opacity="{self.get_opacity()}"></rect>'
        f.write(f"{ts}{line}\n")
        
        
        
        
class ProEpilogue:
    '''ProEpilogue class'''
    def __init__(self, fname="myPart3Art.html", winTitle="My Art"):
        '''__init__ method'''
        f: IO[str] = open(fname, "w")
        self.f = f
        self.writeHTMLHeader(f, winTitle)
        self.openSVGcanvas(f, 1, (500,300))
        shape_list = create_shapes()
        draw_shapes(self, shape_list)
        self.closeSVGcanvas(f, 1)
        f.close()
        
    def writeHTMLHeader(self, f: IO[str], winTitle: str):
        '''writeHeadHTML method'''
        self.writeHTMLline(f, 0, "<html>")
        self.writeHTMLline(f, 0, "<head>")
        self.writeHTMLline(f, 1, f"<title>{winTitle}</title>")
        self.writeHTMLline(f, 0, "</head>")
        self.writeHTMLline(f, 0, "<body>")
        
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
        
    
        
    
def draw_shapes(canvas, shape_list):
    '''draw_shapes method'''
    for shape in shape_list:
        shape.draw_shape(canvas.f)
        
        
def create_shapes():
    '''create_shapes method'''
    shape_list = []
    
    shape_list.append(Circle((50,50,50), (255,0,0,1.0)))
    shape_list.append(Circle((150,50,50), (255,0,0,1.0)))
    shape_list.append(Circle((250,50,50), (255,0,0,1.0)))
    shape_list.append(Circle((350,50,50), (255,0,0,1.0)))
    shape_list.append(Circle((450,50,50), (255,0,0,1.0)))
    shape_list.append(Circle((50,250,50), (0,0,255,1.0)))
    shape_list.append(Circle((150,250,50), (0,0,255,1.0)))
    shape_list.append(Circle((250,250,50), (0,0,255,1.0)))
    shape_list.append(Circle((350,250,50), (0,0,255,1.0)))
    shape_list.append(Circle((450,250,50), (0,0,255,1.0)))
    shape_list.append(Rectangle((50,50,150, 50), (30,180,50,1.0)))
    shape_list.append(Rectangle((150,50,50, 180), (30,10,220,1.0)))
    shape_list.append(Rectangle((250,50,150, 50), (30,180,50,1.0)))
    shape_list.append(Rectangle((350,50,50, 180), (30,10,220,1.0)))
    shape_list.append(Rectangle((450,50,150, 50), (30,180,50,1.0)))
    shape_list.append(Rectangle((50,250,50, 180), (0,255,0,1.0)))
    shape_list.append(Rectangle((150,250,150, 50), (130,80,100,1.0)))
    shape_list.append(Rectangle((250,250,50,180), (0,255,0,1.0)))
    shape_list.append(Rectangle((350,250,150, 50), (130,80,100,1.0)))
    shape_list.append(Rectangle((450,250,50,180), (0,255,0,1.0)))
    
    return shape_list



def main():
    '''main method'''
    ProEpilogue(fname="a41.html", winTitle="Part 1")

main()

                                                                                                                                                                                                                                                                                                        
