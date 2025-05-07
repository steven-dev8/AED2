class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def insert(self, pos: int, value):
        if pos >= 0:
            aux = Node(value)

            if self.length == 0:
                self.start = aux
                self.end = aux
            
            elif pos == self.length:
                aux = Node(value)
                self.end.next = aux
                self.end = aux

            elif pos == 0:
                aux.next = self.start
                self.start = aux

            else:
                start = self.start
                for i in range(pos):
                    if i == pos - 1:
                        previous = start
                    start = start.next
                aux.next = start
                previous.next = aux

            self.length += 1
            return True
        else:
            return False
        
    def print(self):
        element = self.start
        if element != None:
            print("[", end="")
            while element.next != None:
                print(element.value, end=", ")
                element = element.next

            if element.next == None:
                print(element.value, end="")
                print("]")

    def get_value(self, pos: int):
        element = self.start

        if element != None:
            for i in range(self.length):
                if i == pos:
                    return element.value
                else:
                    element = element.next
        return None
    
    def search(self, value):
        element = self.start

        if element != None:
            for i in range(self.length):
                if element.value == value:
                    return i
                else:
                    element = element.next
        return None

    def remove(self, pos):
        if pos + 1 <= self.length and pos >= 0:
            if pos == 0:
                if self.length == 1:
                    self.end = None
                self.start = self.start.next
            else:
                aux = self.start
                for i in range(pos - 1):
                    aux = aux.next

                if pos == self.length - 1:
                    self.end = aux

                aux.next = aux.next.next
                self.length -= 1
            return True
        else:
            return False

                

            

my_list = LinkedList()
my_list.insert(1, 40)
my_list.insert(1, 36)
my_list.insert(0, 10)
my_list.insert(3, 90)
my_list.insert(1, 70)
my_list.print()

my_list.remove(4)
my_list.print()
print(my_list.end.value)
