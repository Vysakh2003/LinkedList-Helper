class linkedlist:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedlist_double:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

#singly linked list
def singly_linkedlist(arr):
    for i in range(len(arr)):
        if i==0:
            head = linkedlist(arr[i])
            current = head
        else:
            current.next = linkedlist(arr[i])
            current = current.next
    return head

#circular singly linked list
def circular_singly_linkedlist(arr):
    for i in range(len(arr)):
        if i==0:
            head = linkedlist(arr[i])
            current = head
        else:
            current.next = linkedlist(arr[i])
            current = current.next
        if i==len(arr)-1:
            current.next = head
    return head

#doubly linked list
def doubly_linkedlist(arr):
    for i in range(len(arr)):
        if i==0:
            head = linkedlist_double(arr[i])
            current = head
        else:
            next_current = linkedlist_double(arr[i])
            current.next = next_current
            next_current.prev = current
            current = next_current
    return head

#circular doubly linked list
def circular_doubly_linkedlist(arr):
    for i in range(len(arr)):
        if i==0:
            head = linkedlist_double(arr[i])
            current = head
        else:
            next_current = linkedlist_double(arr[i])
            current.next = next_current
            next_current.prev = current
            current = next_current
        if i==len(arr)-1:
            current.next = head
            head.prev = current
    return head

#displaying a singly and doubly linked lists
def display_linkedlist(head):
    pointer = head
    while pointer.next:
        print(pointer.val, end=" -> ")
        pointer = pointer.next
    print(pointer.val, end=" ")

#displaying a circular linked lists
def display_circular_linkedlist(head):
    pointer = head
    while True and not None:
        print(pointer.val, end=" <-> ")
        pointer = pointer.next
        if pointer.next == head:
            break
    print(pointer.val,end=" ")
    #print(pointer.val,"<->",head.val,"<->",head.next.val,"<->",head.next.next.val,"<-> continues....",end="")
