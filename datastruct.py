class Node:
    __element = None
    __next = None

    def __init__(self, element, nxt):
        self.__element=element
        self.__next=nxt

    def get_element(self):
        return self.__element

    def get_next(self):
        return self.__next

    def toString(self):
        return "Element: {}, Node: {}".format(self.__element, self.__next)

class LinkedList:
    __head = None
    __tail = None

    def addFront(self, e):
        n = Node(e, self.__head)
        self.__head=n;
        if(self.__tail==None):
            self.__tail=n
    def removeFront(self):
        if not (self.__head==None):
            self.__head=self.__head.get_next()
    def first(self):
        if not (self.__head==None):
            return self.__head.get_element()
        return None
    def last(self):
        return self.__tail.get_element()
    def toString(self):
        n = self.__head
        res = ''
        while not (n==None):
            res += n.toString() + '\n'
            n = n.get_next()
        return res;
