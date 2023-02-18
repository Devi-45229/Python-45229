#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class rectangle_file:
    def __init__(self,l,w):
        self.length=l
        self.width=w
        
    def Area(self):
        a=self.length*self.width
        return a
    
    def Perimeter(self):
        p=2*(self.length+self.width)
        return p
        
    def display(self):
        print(f"Length: {self.length} Width: {self.width}")
        print("Area :",self.Area())
        print("Perimeter :",self.Perimeter())

