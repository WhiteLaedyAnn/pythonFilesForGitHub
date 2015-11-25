#!/usr/bin/env python3
#-*- coding: utf8 -*-
def find_max(node): #ф-я нахождения максимума
    max_list = head.something #пусть максимумом будет самый первый элемент
    while(node != None):#пока не кончатся элементы в списке
        if(node.something > max_list):#если элемент больше максимума
                max_list = node.something#он становится максимумом
            node = node.next_element  #и берётся следующий элемент
    return max_list #ф-я возвращает максимальный элемент связного списка
class Element:
    def __init__(self, smthing = None, nxt_element = None):
        self.something = smthing
        self.next_element = nxt_element
r = int(input("\nEnter the size of the list:"))
node = None
print("Enter the elements of the list:")
for i in range(r):
    append = int(input("  ->    "))
    el0 = node
    node = Element(append , el0)
head = node
#Linked list введён
print("\n\n")
#вывод максимума
if(head != None):
    print(find_max(node), 'Maximum')
else:
    print("Empty list\n")
# находит максимальный элемент в связанном списке целых чисел.
