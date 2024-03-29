from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 0
    currentnode = lst.head
    while currentnode is not None:
        count += 1
        currentnode = currentnode.next
    return count 


def llprint(lst):
    """print a finite linked list"""
    node = lst.head
    if node is None:
        print('empty list')
    while node is not None:
        print(node.val, end=' ')
        node = node.next
    print()


if __name__ == "__main__":
    llist = LList()
    append(llist, Node(1))
    append(llist, Node(2))
    append(llist, Node(4))
    append(llist, Node(8))
    append(llist, Node(16))
    append(llist, Node(32))
    append(llist, Node(64))
    append(llist, Node(128))
    append(llist, Node(256))
    append(llist, Node(512))


    print(length(llist))
    llprint(llist)

from genfinite import lst
print(length(lst))    


