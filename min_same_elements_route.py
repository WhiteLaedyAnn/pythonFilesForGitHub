#!/usr/bin/env python3
#-*- coding: utf8 -*-
import sys

class Tree:
    def __init__(self, number=None, left=None, right=None):
        self.number = number
        self.left = left
        self.right = right

def f_route(t, count, e):
   """
   f_route прибавляет к переменной счётчику по одному за прохождение
   """
    if(t == None):
        return float("inf")
    if(t.number == e):
        return count
    else:
        return min(f_route(t.right, count+1, e),f_route(t.left, count+1, e)) 

def main():
    t = Tree(1,Tree(2, Tree(2,None,None),Tree(3,None,None)), Tree(3, Tree(2,None,None), Tree(3,None,None)))
    count = 0
    count = f_route(t, count, int(input("Enter element:")))
    if(float("inf") != count):
        print(count)
    else:
        print("element is not in the tree")
if __name__ == "__main__":
    main()
#=.= code by (ab)
#В неупорядоченном дереве содержится несколько одинаковых элементов. Написать функцию, возвращающую маршрут к ближайшему из них.
