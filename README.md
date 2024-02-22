# Sp24Lab3
class llist:
    def __init__(self):
        self.head = none
        self.tail = none
        self.length = 0

add another attribute to accumulate the length along with the append function
when needed, you can call length big O(1) because length was done simultaneously with append function
add in append function, when append self.length = self.length + 1