#!/usr/bin/env python3
'''Assignment 4 Part 2 template'''
print(__doc__)

import random
from typing import List, Tuple, IO


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
    def __init__(self, viewport_x=1000, viewport_y=900, num_shapes=10):
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
    randoms = GenRandom(500, 500, num_shapes=50)
    randoms.print_table()

main()
